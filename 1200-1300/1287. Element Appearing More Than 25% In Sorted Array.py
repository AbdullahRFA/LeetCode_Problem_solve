"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.



Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
"""
from typing import List
from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n_25 = len(arr) * 0.25
        dct = Counter(arr)
        for k, v in dct.items():
            if v > n_25:
                return k

# -------------------------------
# 🎯 User Input
# -------------------------------
if __name__ == "__main__":
    arr = list(map(int, input("Enter the array elements (space separated): ").split()))
    slv = Solution()
    print("The special integer is:", slv.findSpecialInteger(arr))