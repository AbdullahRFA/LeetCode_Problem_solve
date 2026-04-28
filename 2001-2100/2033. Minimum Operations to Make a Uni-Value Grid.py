'''
2033. Minimum Operations to Make a Uni-Value Grid
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
Return the minimum number of operations required to make all the elements of the grid equal, or -1 if it is not possible.
Example 1:
Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make all the elements of the grid equal to 4 in 4 operations    
(2 -> 4, 6 -> 4, 8 -> 6 -> 4).
Example 2:
Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make all the elements of the grid equal to 3 in 5 operations
(1 -> 2 -> 3, 5 -> 4 -> 3, 2 -> 3, 3).
Example 3:
Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make all the elements of the grid equal.
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^5
1 <= grid[i][j], x <= 10^4


Intuition:
1. The problem can be solved by first checking if it is possible to make all the elements of the grid equal by checking if all the elements have the same remainder when divided by x. If they do not have the same remainder, it means that it is impossible to make all the elements equal and we can return -1. If they do have the same remainder, we can proceed to calculate the minimum number of operations required to make all the elements equal.
2. To calculate the minimum number of operations, we can first convert all the elements of the grid to a 1D array and then sort the array. We can then find the median of the array, which will be the target value that we want to make all the elements equal to. The reason we choose the median is that it minimizes the sum of absolute deviations from the target value. Finally, we can calculate the total number of operations required to make all the elements equal to the median by summing the absolute differences between each element and the median, divided by x.

Approach:
1. We will first convert the 2D grid into a 1D array by iterating through each row and appending the elements to a new array.
2. We will then check if all the elements in the array have the same remainder when divided by x. If they do not have the same remainder, we will return -1.
3. If they do have the same remainder, we will proceed to calculate the minimum number of operations. We will first convert all the elements in the array to their corresponding values after removing the base remainder and dividing by x. This will give us the number of operations required to make each element equal to the base value.
4. We will then sort the array and find the median value. The median will be the target value that we want to make all the elements equal to.
5. Finally, we will calculate the total number of operations required to make all the elements equal to the median by summing the absolute differences between each element and the median, divided by x.

Time Complexity: O(m*n log(m*n)), where m is the number of rows and n is the number of columns in the grid. We will need to sort the array, which takes O(m*n log(m*n)) time.
Space Complexity: O(m*n), where m is the number of rows and n is the number of columns in the grid. We will need to store the elements of the grid in a 1D array, which takes O(m*n) space. In the worst case, if the grid is a complete grid with all elements being the same, we may need to store all elements in the array.
'''


from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        arr = [num for row in grid for num in row]
        
        base = arr[0]%x

        for num in arr:
            if num%x!=base:
                return -1
        
        arr = [(num-base)//x for num in arr]

        arr.sort()

        median = arr[len(arr)//2]

        return sum(abs(num-median) for num in arr)
