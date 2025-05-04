"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false


"""
"""
Anagram
one string is a rearrangement (or permutation) of the other, 
using exactly the same characters with the same frequency.
"""
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)==sorted(t)
        return Counter(s) == Counter(t)
slv = Solution()
s = input("Enter the string 's' : ")
t = input("Enter the string 't' : ")
print(slv.isAnagram(s,t))