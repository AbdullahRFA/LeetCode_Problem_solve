"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
"""
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        fre = {}
        for x in nums:
            fre[x] = fre.get(x,0)+1
        for k,v in fre.items():
            if v == 1:
                return k



slv = Solution()
print(slv.singleNumber([1,2,2,3,3,4,4]))