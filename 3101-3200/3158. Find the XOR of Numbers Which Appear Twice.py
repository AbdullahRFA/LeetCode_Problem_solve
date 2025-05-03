"""
You are given an array nums, where each number in the array appears either once or twice.

Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.



Example 1:

Input: nums = [1,2,1,3]

Output: 1

Explanation:

The only number that appears twice in nums is 1.

Example 2:

Input: nums = [1,2,3]

Output: 0

Explanation:

No number appears twice in nums.

Example 3:

Input: nums = [1,2,2,1]

Output: 3

Explanation:

Numbers 1 and 2 appeared twice. 1 XOR 2 == 3.
"""
"""
✅ Solution Technique

🔧 Tools Used:
	1.	Hash Map (Dictionary): To count the frequency of each number.
	2.	XOR Operation: To compute the XOR of numbers that appear exactly twice.

⸻

✅ Step-by-Step Logic:
	1.	Count Frequencies:
	•	Iterate through the array and keep a count of how many times each number appears using a dictionary.
	2.	Find Numbers that Appear Twice:
	•	For each number in the dictionary, check if it appears exactly twice.
	3.	XOR the Duplicates:
	•	XOR all the numbers that appeared exactly twice.
	•	If no number appears twice, return 0.
"""

from typing import List


class Solution:
    def xorOfDuplicates(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        result = 0
        for num, count in freq.items():
            if count == 2:
                result ^= num

        return result


# Example usage
s = Solution()
print(s.xorOfDuplicates([1, 2, 1, 3]))  # Output: 1
print(s.xorOfDuplicates([1, 2, 3]))  # Output: 0
print(s.xorOfDuplicates([1, 2, 2, 1]))  # Output: 3