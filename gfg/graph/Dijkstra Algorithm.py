'''
Dijkstra's Algorithm
Given a graph with V vertices and E edges, and a source vertex src, find the shortest distance of all the vertices from the source vertex. If it is not possible to reach any vertex then the distance will be -1.
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
V = 3, E = 3
edges = [[0,1,1],[1,2,2],[0,2,3]]
src = 0
Output: 0 1 3
Explanation: Distance of all the vertices from the source vertex 0 are 0, 1, and 3 respectively.
Your Task:
You don't need to read input or print anything. Your task is to complete the function dijkstra() which takes V, E, edges and src as input parameters and returns an array of size V denoting the shortest distance of all the vertices from the source vertex src.
Expected Time Complexity: O((V + E) log V)
Expected Auxiliary Space: O(V)
Constraints: 1 ≤ V ≤ 10^4 and 1 ≤ E ≤ 10^4  

Intuition:
1. We can solve this problem by using Dijkstra's algorithm, which is a popular algorithm for finding the shortest paths from a source vertex to all other vertices in a graph with non-negative edge weights. We will use a priority queue (min-heap) to keep track of the vertices to explore based on their current shortest distance from the source vertex. We will initialize the distances of all vertices to infinity, except for the source vertex which will be set to 0. We will then repeatedly extract the vertex with the smallest distance from the priority queue and update the distances of its adjacent vertices if a shorter path is found.

Approach:
1. We will initialize an adjacency list to represent the graph, where each entry in the list will contain a list of tuples representing the adjacent vertices and the corresponding edge weights.
2. We will initialize a distance array of size V with all values set to infinity, except for the source vertex which will be set to 0.
3. We will initialize a priority queue (min-heap) and add the source vertex along with its distance (which is 0) to the priority queue.
4. We will then enter a loop that continues until the priority queue is empty.
5. In each iteration of the loop, we will extract the vertex with the smallest distance from the priority queue.
6. We will then iterate through the neighbors of the current vertex in the adjacency list. If a shorter path to a neighbor is found (i.e., the distance to the neighbor through the current vertex is less than the previously known distance), we will update the distance of the neighbor in the distance array and add the neighbor along with its updated distance to the priority queue.
7. Finally, we will return the distance array, which contains the shortest distance of all the vertices from
    the source vertex.
    
Time Complexity: O((V + E) log V), where V is the number of vertices and E is the number of edges in the graph. We will need to visit each vertex and each edge at most once, and each operation on the priority queue takes O(log V) time.
Space Complexity: O(V), where V is the number of vertices in the graph. We will need to use an adjacency list to represent the graph, which takes O(V + E) space. However, since we are only interested in the vertices and not the edges, we can consider the space complexity to be O(V). We will also need to use a distance array of size V to keep track of the shortest distance of each vertex from the source vertex, which takes O(V) space.   
'''


import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        adj_list = [[] for _ in range(V)]
        
        for u,v,d in edges:
            adj_list[u].append([v,d])
            adj_list[v].append([u,d])
        
        distance = [float("inf")]*V
        
        distance[src]=0
        
        p_queue = [[0, src]]
        
        while p_queue:
            dis, curr_node = heapq.heappop(p_queue)
            
            if dis > distance[curr_node]:
                continue
            
            for node , d in adj_list[curr_node]:
                dis_tra = d + dis
                if dis_tra < distance[node]:
                    distance[node]=dis_tra
                    p_queue.append([dis_tra, node])
        return distance