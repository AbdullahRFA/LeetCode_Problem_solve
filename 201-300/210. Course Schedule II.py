'''
210. Course Schedule II
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]
Explanation: There is a total of 1 course to take. Since there are no prerequisites, you can take the course in any order. So the correct course order is [0].
Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
There are no duplicate edges.

Intuition:
1. The problem can be represented as a directed graph where each course is a node and there is a directed edge from course bi to course ai if course bi is a prerequisite for course ai. The problem then reduces to finding a topological ordering of the directed graph. A topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering. If there is a cycle in the graph, it means that there are courses that depend on each other, making it impossible to complete all courses. If there is no cycle, it means that it is possible to complete all courses and we can return the topological ordering of the graph.
2. We can use Kahn's Algorithm, which is a breadth-first search (BFS) based algorithm, to find a topological ordering of a directed graph. The idea is to first calculate the in-degrees of all nodes in the graph. We will then start with all nodes that have an in-degree of zero (i.e., nodes with no dependencies) and add them to a queue. We will repeatedly remove nodes from the queue, add them to a result list, and decrease the in-degrees of their neighbors. If any neighbor's in-degree becomes zero, we will add it to the queue. This process continues until the queue is empty. If we have processed all nodes (i.e., the length of the result list is equal to the number of courses), it means there is no cycle in the graph and we can return the result list as the topological ordering. If there are still nodes that have not been processed, it means there is a cycle in the graph and we can return an empty array.


Approach:
1. We will first create an adjacency list to represent the graph and an array to keep track of the in-degrees of each node. We will iterate through the prerequisites and populate the adjacency list and in-degree array accordingly.
2. We will then initialize a queue and add all nodes with an in-degree of zero to the queue.
3. We will initialize a result list to store the nodes in the order they were processed.
4. We will perform a BFS by repeatedly removing nodes from the queue, adding them to the result list, and decreasing the in-degrees of their neighbors. If any neighbor's in-degree becomes zero, we will add it to the queue.
5. After the BFS is complete, we will check if the length of the result list is equal to the number of courses. If it is, it means there is no cycle in the graph and we can return the result list as the topological ordering. Otherwise, it means there is a cycle in the graph and we can return an empty array.

Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites. We will visit each course and prerequisite at most once during the BFS.
Space Complexity: O(V), where V is the number of courses, due to the adjacency list, in-degree array, queue, and the result list. In the worst case, if the graph is a complete directed graph, we may need to store all courses in the queue and result list for the BFS.
'''


from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        indegress =[0]*numCourses

        for u,v in prerequisites:
            adj_list[v].append(u)
            indegress[u]+=1
        
        queue = deque()
        res = []

        for i in range(numCourses):
            if indegress[i]==0:
                queue.append(i)
            
        while queue:
            curr_node = queue.popleft()
            res.append(curr_node)
            for node in adj_list[curr_node]:
                indegress[node]-=1
                if indegress[node]==0:
                    queue.append(node)
        if len(res)==numCourses:
            return res
        
        return []