'''
Directed Graph Cycle Detection
Given a directed graph, check whether the graph contains a cycle or not. A cycle is present in a directed graph if there is a path from a node to itself. The graph is given in the form of an adjacency list. The function should return true if there is a cycle in the graph, else return false.
Example 1:
Input: V = 4, edges = [[0,1],[1,2],[2,0],[1,3]]
Output: true
Explanation: There is a cycle in the graph (0 -> 1 -> 2 -> 0).
Example 2:
Input: V = 4, edges = [[0,1],[1,2],[2,3]]
Output: false
Explanation: There is no cycle in the graph.
Constraints:
1 <= V <= 10^4
0 <= edges.length <= 10^4
0 <= edges[i][j] < V
edges[i][0] != edges[i][1]
There are no duplicate edges.

Solution: DFS with path tracking
1. We can use a depth-first search (DFS) approach to detect cycles in a directed graph. The idea is to keep track of the nodes currently in the path of the DFS. If we encounter a node that is already in the current path, it means we have found a cycle.
2. We will maintain two arrays: one to keep track of visited nodes and another to keep track of the nodes currently in the path. When we start a DFS from an unvisited node, we will mark it as visited and add it to the current path. We will then recursively visit all its neighbors. If we encounter a neighbor that is already in the current path, we have found a cycle and can return true. After exploring all neighbors, we will remove the node from the current path before backtracking.
3. We will repeat this process for all nodes in the graph to ensure that we check for cycles in all disconnected components of the graph.   
Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph. We will visit each node and edge at most once during the DFS.
Space Complexity: O(V), where V is the number of vertices in the graph, due to the visited array, path array, and the recursive call stack for the DFS. In the worst case, if the graph is a complete directed graph, we may need to store all nodes in the call stack for the DFS.


Second Solution: DFS with color marking
1. Another approach to detect cycles in a directed graph is to use color marking. We can use three colors to mark the state of each node: 0 for unvisited, 1 for visiting, and 2 for done. When we start a DFS from an unvisited node, we will mark it as visiting (color 1). We will then recursively visit all its neighbors. If we encounter a neighbor that is already marked as visiting (color 1), it means we have found a cycle and can return true. After exploring all neighbors, we will mark the node as done (color 2) before backtracking.
2. Similar to the first approach, we will repeat this process for all nodes in the graph to ensure that we check for cycles in all disconnected components of the graph.   
Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph. We will visit each node and edge at most once during the DFS.
Space Complexity: O(V), where V is the number of vertices in the graph, due to the visited array (color array) and the recursive call stack for the DFS. In the worst case, if the graph is a complete directed graph, we may need to store all nodes in the call stack for the DFS.        




'''

# First Solution: DFS with path tracking
class Solution:
    def dfs(self, curr_node, vis, adj_list, path):
        vis[curr_node]=1
        path[curr_node]=1
        
        for node in adj_list[curr_node]:
            if vis[node]==1 and path[node]==1:
                return True
            if vis[node]==0:
                if self.dfs(node, vis, adj_list, path):
                    return True
        path[curr_node]=0
        return False
    
    
    def isCyclic(self, V, edges):
        # code here
        
        vis = [0 for _ in range(V)]
        path = [0 for _ in range(V)]
        adj_list = [[] for _ in range(V)]
        
        for u,v in edges:
            adj_list[u].append(v)
            
        
        for v in range(V):
            if vis[v]==0:
                if self.dfs(v,vis,adj_list,path):
                    return True
        return False
        


        # Second Solution: DFS with color marking
# class Solution:
    
#     def dfs(self, node, vis, adj):
#         vis[node] = 1   # visiting
        
#         for nei in adj[node]:
#             if vis[nei] == 1:   # cycle found
#                 return True
#             if vis[nei] == 0:
#                 if self.dfs(nei, vis, adj):
#                     return True
        
#         vis[node] = 2   # done
#         return False
    
    
#     def isCyclic(self, V, edges):
#         vis = [0] * V
#         adj = [[] for _ in range(V)]
        
#         for u, v in edges:
#             adj[u].append(v)
        
#         for i in range(V):
#             if vis[i] == 0:
#                 if self.dfs(i, vis, adj):
#                     return True
        
#         return False