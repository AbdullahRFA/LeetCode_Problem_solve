"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
"""
"""
🔍 Step-by-Step Solution Technique:

🔸 Step 1: Initialize a write pointer at index 0

This pointer keeps track of where the next non-zero element should go.

🔸 Step 2: Traverse the array with a read pointer

Loop through each element:
	•	If the current element is not zero, write it to nums[write]
	•	Then increment write (to move to the next empty spot)

Now all non-zero elements are shifted to the front in order.

🔸 Step 3: Fill remaining positions with 0

After the loop:
	•	The number of zeroes is len(nums) - write
	•	You loop through that many times from the end, and set those positions to 0
"""
from typing import  List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
        write = len(nums)-write
        if write:
            for x in range(1, write+1):
                nums[-x] = 0
slv = Solution()
# nums = [0,1]
nums = [0,1,0,3,12]
slv.moveZeroes(nums)
print(nums)