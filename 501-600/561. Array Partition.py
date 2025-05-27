"""
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.



Example 1:

Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
Example 2:

Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.

"""
"""
💡 Solution Technique (Greedy Algorithm)

Problem Statement:
You’re given 2n integers. Form n pairs such that the sum of the minimum of each pair is maximized.

Approach:
	•	Sort the array in ascending order.
	•	Pair up the elements such that each smallest element goes with the next smallest (i.e., pair: (nums[0], nums[1]), (nums[2], nums[3]), …).
	•	Since the minimum of each pair is the first element (because the list is sorted), we sum every alternate element starting from index 0.

Why it works? (Greedy Justification):
	•	Sorting ensures that the two closest elements are paired, which minimizes loss (because using a bigger number in a pair with a much smaller one wastes the bigger number).
	•	Taking the smaller of each pair after sorting gives the maximum total of those minimums.
"""

from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res


# --------------------------
# 🎯 User Input Handling
# --------------------------
if __name__ == "__main__":
    nums = list(map(int, input("Enter the list of 2n integers (space-separated): ").split()))

    sol = Solution()
    result = sol.arrayPairSum(nums)
    print("Maximum sum of pairs (min(ai, bi)) is:", result)