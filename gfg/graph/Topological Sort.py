'''
Topological Sort
Given a Directed Acyclic Graph with V vertices and E edges, find any Topological Sorting of that Graph.
Example 1:  
Input: V = 6, E = 6, Edges = {{5, 0}, {4, 0}, {5, 2}, {4, 1}, {2, 3}, {3, 1}}
Output: 5 4 2 3 1 0
Explanation: The output 5 4 2 3 1 0 is one of the possible topological sorts of the given graph. Other valid topological sorts for this graph include 4 5 2 3 1 0, 5 4 2 1 3 0, and 4 5 2 1 3 0.
Example 2:
Input: V = 4, E = 3, Edges = {{0, 1}, {1, 2}, {2, 3}}
Output: 0 1 2 3
Explanation: The output 0 1 2 3 is the only possible topological sort of the given graph.
Constraints:
1 <= V <= 10^4
0 <= E <= 10^4
0 <= edges[i][j] < V
edges[i][0] != edges[i][1]
There are no duplicate edges.

Solution: DFS
1. We can use a depth-first search (DFS) approach to perform a topological sort on a directed acyclic graph (DAG). The idea is to visit each node and its neighbors recursively, and after visiting all neighbors, we will add the node to a stack. This way, the nodes will be added to the stack in reverse order of their dependencies. Finally, we can reverse the stack to get the topological sorting of the graph.
2. We will maintain a visited array to keep track of the nodes we have already visited during the DFS. We will also maintain an adjacency list to represent the graph. We will start a DFS from each unvisited node in the graph to ensure that we cover all disconnected components of the graph.

Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph. We will visit each node and edge at most once during the DFS.
Space Complexity: O(V), where V is the number of vertices in the graph, due to the visited array, adjacency list, and the recursive call stack for the DFS. In the worst case, if the graph is a complete directed graph, we may need to store all nodes in the call stack for the DFS.

Second Solution: Kahn's Algorithm (BFS)
1. Another approach to perform a topological sort on a directed acyclic graph (DAG) is to use Kahn's Algorithm, which is a breadth-first search (BFS) based algorithm. The idea is to first calculate the in-degrees of all nodes in the graph. We will then start with all nodes that have an in-degree of zero (i.e., nodes with no dependencies) and add them to a queue. We will repeatedly remove nodes from the queue, add them to the result list, and decrease the in-degrees of their neighbors. If any neighbor's in-degree becomes zero, we will add it to the queue. This process continues until the queue is empty.
2. We will maintain an adjacency list to represent the graph and an array to keep track of the in-degrees of each node. We will also maintain a result list to store the topological sorting of the graph.  

Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph. We will visit each node and edge at most once during the BFS.
Space Complexity: O(V), where V is the number of vertices in the graph, due to the adjacency list, in-degree array, queue, and the result list. In the worst case,
'''


from collections import deque
class Solution:
    # def dfs(self, curr_node,vis, stack, adj_list):
    #     vis[curr_node]=1
    #     for node in adj_list[curr_node]:
    #         if vis[node]==0:
    #             self.dfs(node, vis, stack, adj_list)
    #     stack.append(curr_node)
        
    # def topoSort(self, V, edges):
    #     # Code here
    #     adj_list = [[] for _ in range(V)]
    #     for u,v in edges:
    #         adj_list[u].append(v)
    #     stack = []
    #     vis = [0 for _ in range(V)]
    #     for i in range(V):
    #         if vis[i]==0:
    #             self.dfs(i,vis, stack, adj_list)
    #     return stack[::-1]
        
    
    def topoSort(self, V, edges):
        adj_list=[[] for _ in range(V)]
        indegrees=[0]*V
        
        for u,v in edges:
            adj_list[u].append(v)
            indegrees[v]+=1
        
        queue = deque()
        res = []
        
        for i in range(V):
            if indegrees[i]==0:
                queue.append(i)
        
        while queue:
            curr_node = queue.popleft()
            res.append(curr_node)
            for node in adj_list[curr_node]:
                indegrees[node]-=1
                if indegrees[node]==0:
                    queue.append(node)
        return res
        
        
        
        
        
        
        
        