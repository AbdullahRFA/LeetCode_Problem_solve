'''
462. Minimum Moves to Equal Array Elements II
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal. In one move, you can increment or decrement an element of the array by 1.
Example 1:
Input: nums = [1,2,3]
Output: 2
Explanation: Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:
Input: nums = [1,10,2,9]
Output: 16
Explanation: The optimal solution is to make all elements equal to 5:
[1,10,2,9]  =>  [5,10,2,9]  =>  [5,5,2,9]  =>  [5,5,5,9]  =>  [5,5,5,5]
Constraints:
n == nums.length
1 <= n <= 10^5
-10^9 <= nums[i] <= 10^9

Intuition:
1. The problem can be solved by first sorting the array and then finding the median of the array. The median is the middle element of the sorted array, and it minimizes the sum of absolute deviations from the target value. Therefore, the optimal solution is to make all elements equal to the median. We can then calculate the total number of moves required to make all the elements equal to the median by summing the absolute differences between each element and the median.  

Approach:
1. We will first sort the input array nums.
2. We will then find the median of the sorted array, which will be the target value that we want to make all the elements equal to.
3. Finally, we will calculate the total number of moves required to make all the elements equal to the median by summing the absolute differences between each element and the median.

Time Complexity: O(n log n), where n is the number of elements in the input array. We will need to sort the array, which takes O(n log n) time.
Space Complexity: O(1), since we are sorting the array in place and using only a constant amount of extra space to store the median and the total number of moves. In the worst case, if the input array is already sorted, we may not need to use any extra space at all
'''


from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums)//2]

        return sum(abs(num-median) for num in nums)