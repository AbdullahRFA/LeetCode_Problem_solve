'''
785. Is Graph Bipartite?
Given an undirected graph, return true if and only if it is bipartite.
Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.
The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.
Example 1:
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: We cannot find a way to split the set of nodes into two independent subsets such that every edge has one node in each subset.
Example 2:  
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can find a way to split the set of nodes into two independent subsets such that every edge has one node in each subset.
Subset A: {0, 2}
Subset B: {1, 3}
Constraints:
graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i.
graph[i] will not contain any element twice.

Solution: DFS
1. We can use a depth-first search (DFS) approach to determine if the graph is bipartite. The idea is to try to color the graph using two colors (e.g., 0 and 1) such that no two adjacent nodes have the same color. If we can successfully color the graph, then it is bipartite; otherwise, it is not.
2. We will initialize a visited array (or color array) to keep track of the color assigned to each node. We will iterate through each node in the graph, and if we encounter an unvisited node, we will start a DFS from that node and attempt to color the graph. We will assign the first color (e.g., 0) to the starting node and then recursively attempt to color all its neighbors with the opposite color (e.g., 1). If we encounter a neighbor that has already been colored with the same color as the current node, then the graph is not bipartite, and we can return false.
3. If we successfully color the graph without any conflicts, we will return true at the end.

Time Complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph. We will visit each node and edge at most once during the DFS.
Space Complexity: O(V), where V is the number of vertices in the graph, due to the visited array (or color array) and the recursive call stack for the DFS. In the worst case, if the graph is a complete bipartite graph, we may need to store all nodes in the call stack for the DFS.    
'''


from typing import List


class Solution:
    def dfs(self,curr_node,vis, graph, color):
        vis[curr_node]=color

        for node in graph[curr_node]:
            if vis[node]!=-1:
                if vis[node]==color:
                    return False
            else:
                if not self.dfs(node, vis, graph, 1-color):
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        node = len(graph)
        vis = [-1]*node
        for i in range(node):
            if vis[i]==-1:
                if not self.dfs(i,vis,graph,0):
                    return False
        return True