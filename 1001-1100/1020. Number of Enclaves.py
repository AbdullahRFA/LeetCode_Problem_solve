'''
1020. Number of Enclaves
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell. A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid. Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output:3
Explanation: There are three land cells (2,1), (2,2) and (1,2) that are enclosed by sea and are not on the boundary, therefore they are not reachable from the boundary. There are also land cells (1,0) and (2,0) that are reachable from the boundary, therefore they are not counted. Note that a land cell is not reachable from the boundary if it is not connected to any land cell on the boundary.
Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output:0
Explanation: All land cells are reachable from the boundary, therefore we return 0.
Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 500
- grid[i][j] is either 0 or 1.
Solution: DFS
1. We can use a depth-first search (DFS) approach to solve this problem. We will start from the border cells of the grid and mark all the land cells (1s) that are connected to the border as visited. These land cells cannot be counted as enclaves because they are reachable from the boundary.
2. We will initialize a visited matrix to keep track of the cells we have already processed. We will iterate through the border cells of the grid and for each land cell (1) that we encounter, we will perform a DFS to mark all the connected land cells as visited.
3. After we have marked all the land cells that are connected to the border, we will iterate through the entire grid again and count all the land cells that are not visited (i.e., those that are enclaves). We will also mark these cells as visited to avoid counting them again.    
4. Finally, we will return the count of enclaves as the result.

Time Complexity: O(m*n), where m and n are the dimensions of the grid, since in the worst case we may need to visit every cell in the grid.
Space Complexity: O(m*n) in the worst case due to the visited matrix storing the state of each cell. However, in practice, the space complexity may be less depending on the structure of the grid and the distribution of land and sea cells.  
'''



from typing import List


class Solution:
    def dfs(self,r,c,vis,grid,rows,cols):
        if r< 0 or r==rows or c<0 or c==cols:
            return
        if grid[r][c]==0 or vis[r][c]==1:
            return
        
        vis[r][c]=1

        self.dfs(r-1,c,vis,grid,rows,cols)
        self.dfs(r+1,c,vis,grid,rows,cols)
        self.dfs(r,c-1,vis,grid,rows,cols)
        self.dfs(r,c+1,vis,grid,rows,cols)
        
    def numEnclaves(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        vis = [[0 for _ in range(cols)]for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if r==0 or r==rows-1 or c == 0 or c==cols-1:
                    if grid[r][c]==1 and vis[r][c]==0:
                        self.dfs(r,c,vis,grid,rows,cols)
        
        cnt = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and vis[r][c]==0:
                    cnt+=1
                    vis[r][c]=1
        return cnt

