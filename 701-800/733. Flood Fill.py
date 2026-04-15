'''
733. Flood Fill

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value color, "flood fill" the image. To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the color parameter.
At the end, return the modified image.
Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not connected to the starting pixel by a path of the same color.
Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 2
Output: [[2,2,2],[2,2,2]]
Constraints:
- The length of image and image[0] will be in the range [1, 50].
- The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
- The value of each color in image[i][j] and color will be an integer in [0, 65535].

Solution: DFS 
1. We can use a depth-first search (DFS) approach to solve this problem. We will start from the given starting pixel (sr, sc) and explore all connected pixels that have the same color as the starting pixel.
2. We will define a recursive function `dfs(i, j)` that will take the current pixel coordinates as input. Inside this function, we will check if the current pixel is out of bounds or if its color is different from the initial color. If either of these conditions is true, we will return from the function.
3. If the current pixel is valid, we will change its color to the new color and then recursively call the `dfs` function for its four adjacent pixels (up, down, left, right).
4. We will call the `dfs` function initially with the starting pixel coordinates (sr, sc) and the initial color of that pixel. After the DFS is complete, we will return the modified image.


Time Complexity: O(m*n), where m and n are the dimensions of the image, since in the worst case we may need to visit every pixel in the image.
Space Complexity: O(m*n) in the worst case due to the recursive call stack when all pixels are connected and have the same color. However, in practice, the space complexity may be less depending on the structure of the image and the connectivity of the pixels.

Solution: BFS
1. We can also use a breadth-first search (BFS) approach to solve this problem. We will start from the given starting pixel (sr, sc) and explore all connected pixels that have the same color as the starting pixel using a queue to manage our exploration.
2. We will initialize a queue and add the starting pixel coordinates to it. We will also keep track of the initial color of the starting pixel.
3. We will enter a loop that continues until the queue is empty. In each iteration, we will dequeue a pixel and change its color to the new color. We will then check its four adjacent pixels (up, down, left, right). If any of these adjacent pixels are valid (i.e., within bounds and have the same color as the initial color), we will enqueue their coordinates to the queue for further exploration.
4. After the BFS is complete, we will return the modified image.

Time Complexity: O(m*n), where m and n are the dimensions of the image, since in the worst case we may need to visit every pixel in the image.
Space Complexity: O(m*n) in the worst case due to the queue storing all pixels when all pixels are connected and have the same color. However, in practice, the space complexity may be less depending on the structure of the image and the connectivity of the pixels.


'''



from collections import deque
from copy import deepcopy
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # dfs

        # if image[sr][sc]==color:
        #     return image
        
        # image_copy = deepcopy(image)
        # r = len(image_copy)
        # c = len(image_copy[0])
        # initial_value = image_copy[sr][sc]

        # def dfs(i,j,image_copy,color,initial_value,r,c):
        #     if i<0 or i>=r or j < 0 or j>=c:
        #         return 
        #     if image_copy[i][j] != initial_value:
        #         return
        #     if image_copy[i][j] == color:
        #         return
        #     image_copy[i][j]=color
        #     dfs(i-1,j,image_copy,color,initial_value,r,c)
        #     dfs(i+1,j,image_copy,color,initial_value,r,c)
        #     dfs(i,j+1,image_copy,color,initial_value,r,c)
        #     dfs(i,j-1,image_copy,color,initial_value,r,c)


        # dfs(sr,sc,image_copy,color,initial_value,r,c)

        # return image_copy

        # bfs

        if image[sr][sc]==color:
            return image
        
        queue = deque()
        queue.append((sr,sc))

        copy_image = deepcopy(image)

        initial_value = copy_image[sr][sc]

        r = len(copy_image)
        c = len(copy_image[0])

        while queue:
            i,j = queue.popleft()

            copy_image[i][j] = color

            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_i , new_j = i+dx, j+dy

                if new_i < 0 or new_i>=r or new_j < 0 or new_j>=c:
                    continue
                if copy_image[new_i][new_j]!= initial_value:
                    continue

                queue.append((new_i,new_j))
        return copy_image