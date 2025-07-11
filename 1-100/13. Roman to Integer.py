"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
"""
Technique to Solve

🔍 Algorithm Idea:
	1.	Create a dictionary to store values of all Roman numerals.
	2.	Loop through each character in the string s.
	3.	For each character:
	•	If the current symbol is smaller than the next one → subtract it.
	•	Else → add it.

This is because subtractive pairs (like IV, IX) always place a smaller numeral before a larger one.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        l = len(s)
        res = 0
        for i in range(1, l):
            if hash_map[s[i - 1]] >= hash_map[s[i]]:
                res += hash_map[s[i - 1]]
            else:
                res -= hash_map[s[i - 1]]
        res += hash_map[s[l - 1]]
        return res

# Get user input and call the function
if __name__ == "__main__":
    user_input = input("Enter a Roman numeral: ").strip().upper()
    sol = Solution()
    result = sol.romanToInt(user_input)
    print(f"The integer value of {user_input} is: {result}")