"""
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""
"""
✅ Step-by-Step Solution Technique

🔹 Problem:

Given a string s, return the longest palindromic substring in s.

⸻

🔸 Step 1: Understand Palindromes

A palindrome is a sequence that reads the same forwards and backwards (like racecar, aba, or bb).

⸻

🔸 Step 2: Expand Around Center Approach

Every palindrome is centered around a character (or between two characters).
We check odd-length and even-length palindromes:
	•	Odd: checkpalindrom(x, x)
	•	Even: checkpalindrom(x, x+1)

⸻

🔸 Step 3: Expand While Valid

In checkpalindrom(l, r), expand as long as:
	•	l >= 0, r < len(s)
	•	s[l] == s[r]

Once the condition fails, return the actual palindromic boundaries: l+1 and r-1.

⸻

🔸 Step 4: Track Longest

After getting bounds from both odd/even checks, compare with previous best length and update start and end.

⸻

🔸 Step 5: Return Result

Return s[start:end+1] — the longest palindromic substring found.

⸻

🧠 Time and Space Complexity
	•	Time Complexity: O(n^2) — we expand around each center
	•	Space Complexity: O(1) — no extra space used (besides variables)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0

        def checkpalindrom(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        for x in range(len(s)):
            l1, r1 = checkpalindrom(x, x)       # Odd length palindrome
            l2, r2 = checkpalindrom(x, x + 1)   # Even length palindrome

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]

# -------- User Input --------
if __name__ == "__main__":
    s = input("Enter the string: ")
    sol = Solution()
    print("Longest Palindromic Substring:", sol.longestPalindrome(s))
