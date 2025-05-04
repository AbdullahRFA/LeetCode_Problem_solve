"""
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
"""
✅ Step-by-step Logic:
	1.	Initialize:
	•	left = 0: start of the window
	•	char_set = set(): to store unique characters in the current window
	•	max_len = 0: to store the maximum length found so far
	2.	Loop through each character (right):
	•	If the character is already in the set, it means there’s a duplicate.
	•	So, shrink the window from the left by removing characters until the duplicate is removed.
	•	Add the current character to the set.
	•	Update the maximum length as right - left + 1.

🚀 Time & Space Complexity:
	•	Time Complexity: O(n), where n is the length of the string — each character is processed at most twice.
	•	Space Complexity: O(k), where k is the number of unique characters in the string.
"""
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


# Take input from user
user_input = input("Enter a string: ")

# Create an instance of Solution and call the method
solution = Solution()
result = solution.lengthOfLongestSubstring(user_input)

print("Length of the longest substring without repeating characters:", result)


