"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true



Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
from collections import  Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map_st={}
        map_ts = {}
        for char_s, char_t in zip(s,t):
            if char_s in map_st:
                if map_st[char_s] != char_t:
                    return False
            map_st[char_s] = char_t
            if char_t in map_ts:
                if map_ts[char_t] != char_s:
                    return False
            map_ts[char_t] = char_s
        print(map_st)
        print(map_ts)
        return True

slv = Solution()
s = "foo"
t = "bar"

# s = "bbbaaaba"
# t = "aaabbbba"
print(slv.isIsomorphic(s,t))