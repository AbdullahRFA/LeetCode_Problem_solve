"""
Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.

To separate the digits of an integer is to get all the digits it has in the same order.

For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].


Example 1:

Input: nums = [13,25,83,77]
Output: [1,3,2,5,8,3,7,7]
Explanation:
- The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.
Example 2:

Input: nums = [7,1,3,9]
Output: [7,1,3,9]
Explanation: The separation of each integer in nums is itself.
answer = [7,1,3,9].

"""
"""
🧠 Solution Technique Explained:
	1.	Input Parsing:
	•	The user provides a list of integers (e.g., 13 25 4 7), which are parsed into a list: [13, 25, 4, 7].
	2.	Iterate Through the List:
	•	For each number x in the list:
	•	If x has more than one digit, convert it to a string, break it into individual characters, convert them back to integers, and extend the result list.
	•	If it’s a single-digit number, just append it directly.
	3.	Build the Final Result List:
	•	All digits (whether from single-digit or multi-digit numbers) are gathered in order.
"""
from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if len(str(x)) > 1:
                temp = [int(d) for d in str(x)]  # Separate each digit
                res.extend(temp)  # Add to result
            else:
                res.append(x)  # Single digit, add directly
        return res


# === User Input ===
nums = list(map(int, input("Enter a list of numbers separated by space: ").split()))

# === Solve and Output ===
slv = Solution()
result = slv.separateDigits(nums)
print("Separated digits:", result)