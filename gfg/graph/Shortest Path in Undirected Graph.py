'''
Shortest Path in Undirected Graph

Given an undirected graph with V vertices and E edges, and a source vertex src, find the shortest distance of all the vertices from the source vertex src. If it is not possible to reach any vertex then the distance will be -1.
Example 1:
Input:
V = 4, E = 4
edges = [[0,1],[0,2],[1,2],[1,3]]
src = 0
Output: 0 1 1 2
Explanation: Distance of all the vertices from the source vertex 0 are 0, 1, 1, and 2 respectively.
Example 2:
Input:
V = 5, E = 6
edges = [[0,1],[0,2],[0,3],[1,2],[1,4],[2,3]]
src = 0
Output: 0 1 1 1 2
Explanation: Distance of all the vertices from the source vertex 0 are 0, 1, 1, 1, and 2 respectively.
Example 3:  
Input:
V = 5, E = 6
edges = [[0,1],[0,2],[0,3],[1,2],[1,4],[2,3]]
src = 0
Output: 0 1 1 1 2
Explanation: Distance of all the vertices from the source vertex 0 are 0, 1, 1, 1, and 2 respectively.

Your Task:
You don't need to read input or print anything. Your task is to complete the function shortestPath() which takes V, E, edges and src as input parameters and returns an array of size V denoting the shortest distance of all the vertices from the source vertex src.  
Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)
Constraints: 1 ≤ V ≤ 10^4 and 1 ≤ E ≤ 10^4

Intuition:
1. We can solve this problem by using a breadth-first search (BFS) approach. We will use a queue to keep track of the vertices that we need to visit, along with their corresponding distances from the source vertex. We will start from the source vertex and keep track of the distances of all the vertices from the source vertex. If we reach a vertex that has not been visited before, we will add it to the queue along with its distance from the source vertex (i.e., distance of the current vertex + 1). We will continue this process until we have visited all the vertices that are reachable from the source vertex.

Approach:
1. We will initialize a distance array of size V with all values set to -1, which will keep track of the shortest distance of each vertex from the source vertex. We will also initialize an adjacency list to represent the graph.
2. We will iterate through the edges array and populate the adjacency list for the graph.
3. We will initialize a queue and add the source vertex along with its distance (which is 0) to the queue. We will also set the distance of the source vertex to 0 in the distance array.
4. We will then enter a loop that continues until the queue is empty.
5. In each iteration of the loop, we will dequeue a vertex and its corresponding distance from the queue.
6. We will then iterate through the neighbors of the current vertex in the adjacency list. If a neighbor has not been visited before (i.e., its distance is -1), we will add it to the queue along with its distance from the source vertex (i.e., distance of the current vertex + 1). We will also update the distance of the neighbor in the distance array.
7. Finally, we will return the distance array, which contains the shortest distance of all the vertices from the source vertex.

Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph. We will need to visit each vertex and each edge at most once, which takes O(V + E) time.
Space Complexity: O(V), where V is the number of vertices in the graph. We will need to use an adjacency list to represent the graph, which takes O(V + E) space. However, since we are only interested in the vertices and not the edges, we can consider the space complexity to be O(V). We will also need to use a distance array of size V to keep track of the shortest distance of each vertex from the source vertex, which takes O(V) space.   


'''


from collections import deque
class Solution:
    def shortestPath(self, V, edges, src):
        # code here
        distance = [-1]*V
        adj_node = [[] for _ in range(V)]
        
        for u,v in edges:
            adj_node[u].append(v)
            adj_node[v].append(u)
            
        queue = deque()
        
        queue.append([src,0])
        distance[src]=0
        
        while queue:
            curr_node, dis = queue.popleft()
            
            dis+=1
            
            for node in adj_node[curr_node]:
                if distance[node]==-1:
                    queue.append([node,dis])
                    distance[node]=dis
        
        return distance
        
