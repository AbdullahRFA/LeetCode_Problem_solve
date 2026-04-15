'''
542. 01 Matrix
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell. The distance between two adjacent cells is 1.
Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,1,1]]
Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 10^4
- 1 <= m * n <= 10^4
- mat[i][j] is either 0 or 1.
Follow up: Could you solve it in linear time and space?

Solution: BFS
1. We can use a breadth-first search (BFS) approach to solve this problem efficiently. We will start from all the cells that contain 0 and explore their neighbors to calculate the distance to the nearest 0 for each cell.
2. We will initialize a queue and add all the cells that contain 0 to the queue, along with their initial distance (which is 0). We will also maintain a visited matrix to keep track of the cells we have already processed.
3. We will enter a loop that continues until the queue is empty. In each iteration, we will dequeue a cell and check its four adjacent cells (up, down, left, right). If any of these adjacent cells are valid (i.e., within bounds and not visited), we will mark them as visited, calculate their distance as the distance of the current cell plus one, and enqueue them for further exploration.
4. After the BFS is complete, we will have the distance to the nearest 0 for each cell in the distance matrix, which we will return as the result.  

Time Complexity: O(m*n), where m and n are the dimensions of the matrix, since in the worst case we may need to visit every cell in the matrix.
Space Complexity: O(m*n) in the worst case due to the queue storing all cells when all cells are 1 and we need to visit them to calculate their distance to the nearest 0. However, in practice, the space complexity may be less depending on the structure of the matrix and the distribution of 0s and 1s.
'''


from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])

        vis = [[0 for _ in range(c)]for _ in range(r)]
        dis = [[0 for _ in range(c)]for _ in range(r)]

        queue = deque()

        for i in range(r):
            for j in range(c):
                if mat[i][j]==0:
                    queue.append([i,j,0])
                    vis[i][j] = 1
        

        while queue:
            i,j,d=queue.popleft()
            dis[i][j]=d
            for x ,y in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_i,new_j=i+x,j+y

                if new_i<0 or new_i>=r or new_j<0 or new_j>=c:
                    continue
                if vis[new_i][new_j]==1:
                    continue
                vis[new_i][new_j]=1
                queue.append([new_i,new_j,d+1])

        return dis
