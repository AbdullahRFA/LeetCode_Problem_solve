'''
994. Rotting Oranges
In a given grid, each cell can have one of three values:
the value 0 representing an empty cell,
the value 1 representing a fresh orange, or
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.
Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2.


Solution: BFS
1. We can use a breadth-first search (BFS) approach to solve this problem. We will start by adding all the rotten oranges (value 2) to a queue and counting the number of fresh oranges (value 1) in the grid.
2. We will then perform a BFS traversal from the rotten oranges. For each rotten orange, we will check its four adjacent cells (up, down, left, right). If any of the adjacent cells contain a fresh orange, we will rot that orange (change its value to 2), decrease the count of fresh oranges, and add the newly rotten orange to the queue.
3. We will keep track of the number of minutes that elapse during the BFS traversal. Each time we process all the rotten oranges in the queue, we will increment the minutes by 1.
4. The BFS traversal will continue until there are no more rotten oranges to process or until there are no fresh oranges left. If there are still fresh oranges left after the BFS traversal, we will return -1. Otherwise, we will return the number of minutes that elapse.

Time Complexity: O(m*n), where m is the number of rows and n is the number of columns in the grid, since we may need to visit each cell in the grid at most once.
Space Complexity: O(m*n), in the worst case, if all oranges are rotten, we may need to store all the rotten oranges in the queue. However, since the grid size is limited to 10x10, the space complexity can be considered O(1) for practical purposes.


'''


from collections import deque
from copy import deepcopy
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        grid_copy = deepcopy(grid)

        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid_copy[r][c] == 2:
                    queue.append((r,c))
                elif grid_copy[r][c] == 1:
                    fresh+=1
                    

        minutes = 0

        while queue and fresh > 0:
            total_rotten = len(queue)
            minutes+=1

            for _ in range(total_rotten):
                i,j = queue.popleft()

                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:

                    new_i, new_j = i+dx, j+dy

                    if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
                        continue
                    if grid_copy[new_i][new_j] == 0 or grid_copy[new_i][new_j] == 2:
                        continue
                    
                    fresh -= 1
                    grid_copy[new_i][new_j] = 2
                    queue.append((new_i, new_j))
        
        return -1 if fresh > 0 else minutes

        