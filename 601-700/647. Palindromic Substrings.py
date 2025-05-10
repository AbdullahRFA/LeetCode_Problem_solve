"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""
"""
🧠 Step-by-Step Solution Technique:

🔸 Problem Understanding:
	•	You’re given a string s.
	•	You need to count all substrings that are palindromes.
	•	Substrings must be contiguous.
	•	Single characters like 'a', 'b' are also palindromes.

⸻

✅ Step-by-Step Explanation:

Step 1: Expand Around Center
	•	A palindrome reflects around its center.
	•	Each character in the string can act as the center of a palindrome.
	•	We also consider the gap between characters for even-length palindromes.

Step 2: Two Loops in One

For every index x in the string:
	•	Treat s[x] as the center of an odd-length palindrome and expand around it.
	•	Treat the gap between s[x] and s[x+1] as the center of an even-length palindrome and expand around that.

Step 3: Expand While Matching
	•	From each center, expand outward (l--, r++) as long as characters match.
	•	Every time characters match, count it as a valid palindrome substring.

⸻

🧮 Example Dry Run: Input "aaa"
	•	Centers checked: (0,0), (0,1), (1,1), (1,2), (2,2)
	•	Palindromes found:
	•	(0,0): “a”
	•	(0,1): “aa”
	•	(0,2): “aaa”
	•	(1,1): “a”
	•	(1,2): “aa”
	•	(2,2): “a”
	•	Total = 6 palindromic substrings

⸻

⏱ Complexity:
	•	Time Complexity: O(n^2) — for each character we may expand up to the whole string.
	•	Space Complexity: O(1) — no extra data structures used.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        def checkpalindrom(l, r):
            palindrom = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindrom += 1
                l -= 1
                r += 1
            return palindrom

        result = 0
        for x in range(len(s)):
            result += checkpalindrom(x, x)      # Odd-length palindromes
            result += checkpalindrom(x, x + 1)  # Even-length palindromes
        return result

# Taking user input
user_input = input("Enter a string: ")
sol = Solution()
print("Number of palindromic substrings:", sol.countSubstrings(user_input))