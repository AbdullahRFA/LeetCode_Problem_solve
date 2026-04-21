'''
200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input: grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
Output: 1
Example 2:
Input: grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
Output: 3
Constraints:
m == grid.length
n == grid[i].length 

1 <= m, n <= 300
grid[i][j] is '0' or '1'.

Solution: BFS
1. We can use a breadth-first search (BFS) approach to solve this problem. We will iterate through each cell in the grid, and whenever we encounter a '1' (land) that has not been visited, we will perform a BFS to mark all connected '1's as visited. This will allow us to count the number of islands in the grid.
2. We will initialize a counter to keep track of the number of islands and a visited matrix to keep track of which cells have been visited. We will iterate through each cell in the grid, and if we encounter a '1' that has not been visited, we will increment the island counter and perform a BFS starting from that cell.
3. In the BFS, we will use a queue to keep track of the cells to be processed. We will enqueue the starting cell and mark it as visited. We will then enter a loop that continues until the queue is empty. Inside the loop, we will dequeue a cell and check its four adjacent cells (up, down, left, right). If any of the adjacent cells contain a '1' and have not been visited, we will enqueue that cell and mark it as visited.
4. After the BFS is complete, we will have marked all the connected '1's as visited, and we can continue iterating through the grid to find the next unvisited '1' to start a new BFS for the next island. We will repeat this process until we have processed all cells in the grid.
5. Finally, we will return the count of islands.

Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid. We will visit each cell at most once during the BFS.
Space Complexity: O(m * n) in the worst case, if the grid is filled with '1's, we will need to store all cells in the queue and the visited matrix.

'''


from collections import deque
from typing import List


class Solution:
    def bfs(self, r,c,vis,grid,rows,cols):
            queue=deque()
            queue.append((r,c))

            while queue:
                i,j=queue.popleft()

                for x, y in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni = i+x
                    nj = j+y

                    if ni < 0 or ni==rows or nj < 0 or nj==cols:
                        continue
                    if grid[ni][nj]=="0":
                        continue
                    if grid[ni][nj] == "1" and vis[ni][nj]==1:
                        continue
                    vis[ni][nj]=1
                    queue.append((ni,nj))
    def numIslands(self, grid: List[List[str]]) -> int:

       

        
        rows = len(grid)
        cols = len(grid[0])

        vis = [[0 for _ in range(cols)] for _ in range(rows)]
        cnt = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and vis[r][c]==0:
                    cnt+=1
                    self.bfs(r,c,vis,grid,rows,cols)
        return cnt