"""
You are given a string s consisting of lowercase English letters, and an integer k. Your task is to convert the string into an integer by a special process, and then transform it by summing its digits repeatedly k times. More specifically, perform the following steps:

Convert s into an integer by replacing each letter with its position in the alphabet (i.e. replace 'a' with 1, 'b' with 2, ..., 'z' with 26).
Transform the integer by replacing it with the sum of its digits.
Repeat the transform operation (step 2) k times in total.
For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above.



Example 1:

Input: s = "iiii", k = 1

Output: 36

Explanation:

The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
Thus the resulting integer is 36.

Example 2:

Input: s = "leetcode", k = 2

Output: 6

Explanation:

The operations are as follows:
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
- Transform #2: 33 ➝ 3 + 3 ➝ 6
Thus the resulting integer is 6.

Example 3:

Input: s = "zbax", k = 2

Output: 8
"""
"""
✅ Problem Summary

Given a string s consisting of lowercase English letters and an integer k, you must:
	1.	Convert each character to its alphabetical position (a = 1, b = 2, …, z = 26).
	2.	Concatenate all the numbers into a single string.
	3.	Repeat k times:
	•	Convert the string to an integer.
	•	Calculate the sum of its digits.
	4.	Return the resulting integer after k transformations.

⸻

💡 Solution Technique Explained

🔸 Step-by-Step Breakdown:
	1.	Character to Alphabet Position
Use ord(x) % 96 to convert characters to their alphabetical position:

ord('a') = 97 ⇒ 97 % 96 = 1
ord('b') = 98 ⇒ 98 % 96 = 2
...
ord('z') = 122 ⇒ 122 % 96 = 26

✅ Alternative: ord(x) - ord('a') + 1 is more readable.

	2.	Build Integer String
Concatenate each alphabet value into one string.
Example:

s = "leetcode"
Alphabet positions: l(12), e(5), e(5), t(20), c(3), o(15), d(4), e(5)
Concatenated: "12552031545"


	3.	Repeat Sum of Digits k Times
For k times, convert the number to digits and add them:

"12552031545" → 1+2+5+5+2+0+3+1+5+4+5 = 33
(next iteration if k > 1): 3+3 = 6



⸻

🧠 Algorithm Type
	•	This is a simulation problem, combining:
	•	ASCII manipulation
	•	String to digit transformation
	•	Digit sum calculation
	•	The overall time complexity is O(n + k * d) where:
	•	n is the length of the string
	•	d is the number of digits in each transformation (usually small)

⸻

✅ Output Example

s = "leetcode"
k = 2

Step 1: leetcode → 12 5 5 20 3 15 4 5 → "12552031545"
Step 2: Sum of digits (1st time): 1+2+5+5+2+0+3+1+5+4+5 = 33
Step 3: Sum of digits (2nd time): 3+3 = 6

Output: 6

"""

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        int_str = ''
        for x in s:
            # print(ord(x)%96)
            # int_str += str(ord(x)%96)
            int_str += str(ord(x) - ord('a') + 1)
        # print(int_str)
        int_num = int(int_str)
        # print(int_num)
        for _ in range(k):
            tem = int_num
            Sum = 0
            while tem != 0:
                Sum += tem%10
                tem //=10
            int_num = Sum
        return int_num

slv = Solution()

# s = "iiii"
# k = 1
s = "leetcode"
k = 2
print(slv.getLucky(s,k))