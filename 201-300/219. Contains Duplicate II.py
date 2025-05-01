"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


🧠 Solution Idea:

We’ll use a dictionary (hash map) to track the last index of each value we see.

Steps:
	1.	Loop through the array.
	2.	For each element:
	    •	If it was seen before, check the difference between current index and last seen index.
	    •	If abs(i - last_index) <= k, return True.
	3.	If no such pair is found, return False.

Example Walkthrough:

For input nums = [1, 0, 1, 1], k = 1:
	•	i = 0 → x = 1: not seen before → store 1: 0
	•	i = 1 → x = 0: not seen before → store 0: 1
	•	i = 2 → x = 1: seen before at index 0 → 2 - 0 = 2 > 1 → not valid → update to 1: 2
	•	i = 3 → x = 1: seen before at index 2 → 3 - 2 = 1 <= 1 → ✅ return True
"""

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = {}
        ans = False
        for i, x in enumerate(nums):
            if x in check:
                if abs(i - check[x]) <= k:
                    ans = True
                    break  # Early exit if condition met
            check[x] = i  # Always update latest index
        return ans


# Example usage
sol = Solution()

# Example 1
print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))      # Output: True

# Example 2
print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))      # Output: True

# Example 3
print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # Output: False

"""
🧠 Quick Recap:
	•	I use a dictionary check to store the last index of each element.
	•	If a duplicate is found within distance k, ans is set to True and loop breaks.
	•	You must update check[x] = i every iteration to ensure latest index is tracked.
"""