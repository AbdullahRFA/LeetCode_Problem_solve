"""
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.


"""
"""
🧠 Explanation:
	•	Sort the array to bring close values together.
	•	Slide a window of size k across the sorted array.
	•	In each window, compute the difference between max and min (which are at the ends of the window due to sorting).
	•	Keep track of the minimum of all these differences.
"""
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0  # No difference if only one number in a group

        nums.sort()
        min_diff = float('inf')
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, diff)
        return min_diff


# --------------------------
# 🎯 User Input Handling
# --------------------------
if __name__ == "__main__":
    nums = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
    k = int(input("Enter the value of k: "))

    sol = Solution()
    result = sol.minimumDifference(nums, k)
    print("Minimum difference between highest and lowest of k scores:", result)