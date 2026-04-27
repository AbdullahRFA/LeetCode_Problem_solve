'''
802. Find Eventual Safe States
In a directed graph, we start at some node and every turn, walk along a directed edge of the graph. If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.  Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps. 
Return an array containing all the eventually safe nodes of the graph.  The answer should be sorted in ascending order.
Example 1:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
The nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all eventually reach nodes 5 or 6.
Example 2:  
Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation: The given graph is shown above.
The only terminal node is 4.
Every path starting at node 4 reaches node 4, so the only eventually safe node is node 4.
Constraints:
graph will have length at most 10000.
The number of edges in the graph will not exceed 32000.
Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].   

Intuition:
1. The problem can be represented as a directed graph where each node represents a state and there is a directed edge from node u to node v if there is a transition from state u to state v. The problem then reduces to finding all nodes that are eventually safe, which means that there is no cycle in the graph that can be reached from those nodes. If there is a cycle in the graph, it means that there are states that depend on each other, making it impossible to reach a terminal node. If there is no cycle, it means that it is possible to reach a terminal node and we can return those nodes as eventually safe nodes.
2. We can use Kahn's Algorithm, which is a breadth-first search (BFS) based algorithm, to find all nodes that are eventually safe. The idea is to first calculate the in-degrees of all nodes in the graph. We will then start with all nodes that have an in-degree of zero (i.e., nodes with no dependencies) and add them to a queue. We will repeatedly remove nodes from the queue, add them to a result list, and decrease the in-degrees of their neighbors. If any neighbor's in-degree becomes zero, we will add it to the queue. This process continues until the queue is empty. If we have processed all nodes, it means there is no cycle in the graph and we can return the result list as the eventually safe nodes. If there are still nodes that have not been processed, it means there is a cycle in the graph and we can return an empty array.

Approach:
1. We will first create an adjacency list to represent the graph and an array to keep track of the in-degrees of each node. We will iterate through the graph and populate the adjacency list and in-degree array accordingly.
2. We will then initialize a queue and add all nodes with an in-degree of zero to the queue.
3. We will initialize a result list to store the nodes in the order they were processed.
4. We will perform a BFS by repeatedly removing nodes from the queue, adding them to the result list, and decreasing the in-degrees of their neighbors. If any neighbor's in-degree becomes zero, we will add it to the queue.
5. After the BFS is complete, we will sort the result list and return it as the eventually safe nodes.

Time Complexity: O(V + E), where V is the number of nodes and E is the number of edges. We will visit each node and edge at most once during the BFS.
Space Complexity: O(V), where V is the number of nodes, due to the adjacency list, in-degree array, queue, and the result list. In the worst case, if the graph is a complete directed graph, we may need to store all nodes in the queue and result list for the BFS.
'''


from collections import deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        adj_list = [[]for _ in range(V)]
        indegress = [0]*V

        for node in range(V):
            for adj in graph[node]:
                adj_list[adj].append(node)
                indegress[node]+=1
        
        queue = deque()

        for node in range(V):
            if indegress[node]==0:
                queue.append(node)
        
        res = []

        while queue:
            curr_node = queue.popleft()
            res.append(curr_node)
            for node in adj_list[curr_node]:
                indegress[node]-=1
                if indegress[node]==0:
                    queue.append(node)
        res.sort()
        return res