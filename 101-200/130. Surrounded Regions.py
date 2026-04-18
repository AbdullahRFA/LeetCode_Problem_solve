'''
130. Surrounded Regions
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in that surrounded region.
Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:
Input: board = [["X"]]
Output: [["X"]]
Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.

Solution: DFS
1. We can use a depth-first search (DFS) approach to solve this problem. We will start from the border cells of the board and mark all the 'O's that are connected to the border as visited. These 'O's cannot be flipped to 'X' because they are not surrounded by 'X'.
2. We will initialize a visited matrix to keep track of the cells we have already processed. We will iterate through the border cells of the board and for each 'O' that we encounter, we will perform a DFS to mark all the connected 'O's as visited.
3. After we have marked all the 'O's that are connected to the border, we will iterate through the entire board again and flip all the 'O's that are not visited (i.e., those that are surrounded by 'X') to 'X'. We will also mark these cells as visited to avoid processing them again.
4. Finally, we will return the modified board as the result.

Time Complexity: O(m*n), where m and n are the dimensions of the board, since in the worst case we may need to visit every cell in the board.
Space Complexity: O(m*n) in the worst case due to the visited matrix storing the state of each cell. However, in practice, the space complexity may be less depending on the structure of the board and the distribution of 'X' and 'O'.
'''

from typing import List


class Solution:


    def dfs(self,r,c,vis,board,rows,cols):
        if r < 0 or r==rows or c<0 or c==cols:
            return
        if vis[r][c]==1:
            return
        if board[r][c]=="X":
            return
        
        vis[r][c]=1
        self.dfs(r-1,c,vis,board,rows,cols)
        self.dfs(r+1,c,vis,board,rows,cols)
        self.dfs(r,c-1,vis,board,rows,cols)
        self.dfs(r,c+1,vis,board,rows,cols)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        vis = [[0 for _ in range(cols) ]for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if r == 0 or r==rows-1 or c == 0 or c==cols-1:
                    if vis[r][c] == 0 and board[r][c]=="O":
                        self.dfs(r,c,vis,board,rows,cols)
        
        for r in range(rows):
            for c in range(cols):
                if vis[r][c]==0 and board[r][c]=="O":
                    board[r][c]="X"
                    vis[r][c]=1