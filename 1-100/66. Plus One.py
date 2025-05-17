"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""
"""
🧠 Solution Technique:

Goal:
Given a list of digits representing a non-negative integer, add 1 to the integer and return the result as a list of digits.

⸻

⚙️ Steps:
	1.	Convert digits to string:
	•	Join the digits to form a single string representing the number.
	•	Example: [1, 2, 3] → "123"
	2.	Convert string to integer:
	•	Use int() to convert the string to an integer.
	•	"123" → 123
	3.	Add one:
	•	Perform the addition.
	•	123 + 1 → 124
	4.	Convert back to list of digits:
	•	Turn the result back into a string, then convert each character back to an integer.
	•	"124" → [1, 2, 4]

⸻

🕒 Time and Space Complexity:
	•	Time Complexity: O(n)
Where n is the number of digits. All operations (conversion, string/number manipulation) are linear.
	•	Space Complexity: O(n)
New list of digits is created as output.
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ""
        for x in digits:
            temp += str(x)
        num = int(temp) + 1
        return [int(x) for x in str(num)]


# ---- Main Function for User Input ----
if __name__ == "__main__":
    # Example input format: 1 2 3
    user_input = input("Enter digits separated by space: ")
    digits = list(map(int, user_input.strip().split()))

    solution = Solution()
    result = solution.plusOne(digits)

    print("Result after plus one:", result)