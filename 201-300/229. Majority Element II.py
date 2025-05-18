"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.



Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
"""
from collections import Counter
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)/3
        res = []
        dct = Counter(nums)
        for k,v in dct.items():
            if v>n:
                res.append(k)
        return res
slv = Solution()
nums = [1,2]
print(slv.majorityElement(nums))