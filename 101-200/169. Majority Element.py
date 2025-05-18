"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""
"""
🧠 Solution Technique

Problem Statement:

Given an array nums, return the majority element — the element that appears more than ⌊n / 2⌋ times.
It is guaranteed that the majority element always exists in the array.

⸻

⚙️ How It Works:
	1.	Count Frequencies:
	•	The Counter(nums) from collections builds a dictionary where the keys are the elements of the array and the values are their counts.
	2.	Check for Majority:
	•	The majority element will have a frequency greater than half the length of the list (n/2).
	•	Iterate through the dictionary and return the element with count > n // 2.

⸻

🕒 Time and Space Complexity
	•	Time Complexity: O(n) – where n is the length of the array.
	•	It goes through the array once to count frequencies and then through the dictionary.
	•	Space Complexity: O(n) – extra space is used to store counts in the dictionary.

"""
from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2  # Integer division
        dct = Counter(nums)  # Count frequency of each element
        for k, v in dct.items():
            if v > n:
                return k

# -------- Main function for user input ----------
if __name__ == "__main__":
    nums = list(map(int, input("Enter elements of the array (space separated): ").strip().split()))
    solution = Solution()
    result = solution.majorityElement(nums)
    print("Majority element is:", result)