"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []

"""

from typing import  List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # dct = Counter(nums)
        # res = []
        # for k,v in Counter(nums).items():
        #     if v == 2:
        #         res.append(k)

        # return res

        res = []
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] < 0:
                res.append(abs(x))
            else:
                nums[idx] = -nums[idx]
        return res

slv = Solution()
nums = [4,3,2,7,8,2,3,1]
print(slv.findDuplicates(nums))