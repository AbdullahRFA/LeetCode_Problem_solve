"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
"""
💡 Idea:
	•	When strings are sorted lexicographically, the smallest and largest strings will contain the maximum possible difference in characters.
	•	So, the common prefix of the entire array must also be the common prefix of the first and last strings in the sorted list.

🔁 Step-by-Step:
	1.	Sort the list of strings:
	•	["flower", "flow", "flight"] → ["flight", "flow", "flower"]
	2.	Compare the first and last strings:
	•	First: "flight", Last: "flower"
	3.	Loop character by character:
	•	'f' == 'f', 'l' == 'l'
	•	'i' != 'o' → Stop here
	4.	Return "fl" → the longest common prefix
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]

# -------- User Input --------
str_list = input("Enter strings separated by space: ").split()
s = Solution()
print("Longest Common Prefix:", s.longestCommonPrefix(str_list))