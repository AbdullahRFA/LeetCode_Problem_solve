"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

🔹 Step-by-step logic:
	1.	A list can contain duplicates, but a set only keeps unique elements.
	2.	When you do set(nums), all duplicates are automatically removed.
	3.	If the size of the set is smaller than the size of the original list, it means some elements were removed → duplicates existed.
💡 Time Complexity
	•	Converting to a set: O(n)
	•	Comparing lengths: O(1)
✅ Overall time: O(n)

"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_num = set(nums)  # Convert the list to a set (removes duplicates)
        return len(set_num) < len(nums)  # If set is smaller, duplicates exist


# Example usage
sol = Solution()

# Test cases
print(sol.containsDuplicate([1, 2, 3, 4]))      # Output: False (no duplicates)
print(sol.containsDuplicate([1, 2, 3, 1]))      # Output: True (1 is duplicated)
print(sol.containsDuplicate([5, 5, 5, 5]))      # Output: True (all are the same)