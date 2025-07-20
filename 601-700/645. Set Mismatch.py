"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.



Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]

"""

from typing import List
from collections import  Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dct = Counter(nums)

        n = len(nums)
        nums = set(nums)
        # print(nums)
        # print(n)

        for k, v in dct.items():
            if v == 2:
                twice_num = k
        # missing_number = 0
        for i in range(1, n + 1):
            # print(i)
            if i not in nums:
                missing_number = i

        return [twice_num, missing_number]
slv = Solution()
nums = [1,2,2,4]
print(slv.findErrorNums(nums))

