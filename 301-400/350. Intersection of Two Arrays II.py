"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        # for x in nums1:
        #     if x in nums2:
        #         res.append(x)
        #         nums2.remove(x)
        cnter = Counter(nums1)
        for x in nums2:
            if cnter[x]>0:
                res.append(x)
                cnter[x] -= 1
        return res
svl = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(svl.intersect(nums1,nums2))