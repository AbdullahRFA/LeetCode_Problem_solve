#User function Template for python3
'''
Shortest path in Directed Acyclic Graph
Given a Directed Acyclic Graph with V vertices and E edges, and a source vertex src, find the shortest distance of all the vertices from the source vertex src. If it is not possible to reach any vertex then the distance will be -1.
Example 1:
Input:
V = 6, E = 7
edges = [[0,1,2],[0,4,1],[1,2,3],[2,3,6],[4,2,2],[4,5,4],[5,3,1]]
src = 0
Output: 0 2 3 6 1 5     
Explanation: Distance of all the vertices from the source vertex 0 are 0, 2, 3, 6, 1, and 5 respectively.
Example 2:
Input:
V = 5, E = 6
edges = [[0,1,2],[0,2,3],[1,2,1],[1,3,1],[2,3,1],[3,4,2]]   
src = 0
Output: 0 2 3 3 5
Explanation: Distance of all the vertices from the source vertex 0 are 0, 2, 3, 3, and 5 respectively.
Example 3:
Input:
V = 5, E = 6
edges = [[0,1,2],[0,2,3],[1,2,1],[1,3,1],[2,3,1],[3,4,2]]
src = 0
Output: 0 2 3 3 5
Explanation: Distance of all the vertices from the source vertex 0 are 0, 2, 3, 3, and 5 respectively.  


Your Task:
You don't need to read input or print anything. Your task is to complete the function shortestPath() which takes V, E, edges and src as input parameters and returns an array of size V denoting the shortest distance of all the vertices from the source vertex src.  
Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)
Constraints: 1 ≤ V ≤ 10^4 and 1 ≤ E ≤ 10^4


Intuition:
1. We can solve this problem by using a depth-first search (DFS) approach to perform a topological sort of the vertices in the graph. Once we have the vertices in topologically sorted order, we can initialize a distance array with infinity values and set the distance of the source vertex to 0. We will then iterate through the vertices in topologically sorted order and update the distances of the adjacent vertices based on the distances of the current vertex. This way, we can ensure that we are always updating the distances of the adjacent vertices based on the shortest distance from the source vertex.

Approach:
1. We will initialize an adjacency list to represent the graph, where each entry in the list will contain a list of tuples representing the adjacent vertices and the corresponding edge weights.
2. We will perform a depth-first search (DFS) to get the vertices in topologically sorted order. We will use a visited array to keep track of the visited vertices and a stack to store the vertices in topologically sorted order.
3. After we have the vertices in topologically sorted order, we will initialize a distance array of size V with all values set to infinity, except for the source vertex which will be set to 0.
4. We will then iterate through the vertices in topologically sorted order and for each vertex, we will update the distances of its adjacent vertices based on the edge weights.
5. Finally, we will iterate through the distance array and replace any remaining infinity values with -1 to indicate that those vertices are not reachable from the source vertex. We will return the distance array as the final answer.

Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph. We will need to visit each vertex and each edge at most once, which takes O(V + E) time.
Space Complexity: O(V), where V is the number of vertices in the graph. We will need to use an adjacency list to represent the graph, which takes O(V + E) space. However, since we are only interested in the vertices and not the edges, we can consider the space complexity to be O(V). We will also need to use a distance array of size V to keep track of the shortest distance of each vertex from the source vertex, which takes O(V) space.


'''


from typing import List

class Solution:
    
    def dfs(self,node, vis, adj_list, stack):
        vis[node]=1
        
        for adjNode , d in adj_list[node]:
            if vis[adjNode]==0:
                self.dfs(adjNode, vis, adj_list, stack)
        stack.append(node)

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(V)]
        
        for u,v,d in edges:
            adj_list[u].append([v,d])
        
        vis = [0]*V
        stack = []
        
        for node in range(V):
            if vis[node]==0:
                self.dfs(node, vis, adj_list, stack)
                
        distance = [float("inf")]*V
        distance[0]=0
        
        while stack:
            node = stack.pop()
            dis = distance[node]
            
            for adjNode, d in adj_list[node]:
                newD = d + dis
                if newD < distance[adjNode]:
                    distance[adjNode]=newD
        for i in range(V):
            if distance[i] == float("inf"):
                distance[i]= -1
        return distance
        
        
            
