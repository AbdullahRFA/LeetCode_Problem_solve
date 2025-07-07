"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.



Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation:
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
"""
from typing import List
from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        fre = defaultdict(int)
        start_idx = {}
        end_idx = {}
        for i, num in enumerate(nums):
            fre[num] += 1
            if num not in start_idx:
                start_idx[num] = i
            end_idx[num] = i

        degree = max(fre.values())
        res = float("inf")
        for num in fre:
            if fre[num] == degree:
                res = min(end_idx[num] - start_idx[num] + 1, res)

        return res

nums = [1,2,2,3,1]
slv = Solution()
print(slv.findShortestSubArray(nums))
"""
🧠 Solution Technique:
	1.	Count frequencies of each number using fre.
	2.	Store the first and last index of each number in start_idx and end_idx.
	3.	Find the degree (maximum frequency).
	4.	For each number with frequency equal to the degree:
	•	Compute subarray length: end_idx - start_idx + 1
	•	Keep the minimum length.
"""