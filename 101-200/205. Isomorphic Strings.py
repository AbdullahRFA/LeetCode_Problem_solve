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
"""
Sure! Here’s a step-by-step breakdown of the correct technique to solve the isomorphic strings problem:

⸻

✅ Problem Recap

Two strings s and t are isomorphic if the characters in s can be replaced to get t such that:
	•	Every occurrence of a character in s must be replaced with the same character in t.
	•	No two different characters in s may map to the same character in t.

⸻

🔍 Step-by-Step Technique

⸻

✅ Step 1: Check Lengths

If the lengths of s and t are not equal, they cannot be isomorphic.

if len(s) != len(t):
    return False


⸻

✅ Step 2: Create Two Dictionaries
	•	One dictionary (mapping_st) to map characters from s → t.
	•	Another dictionary (mapping_ts) to ensure the reverse mapping from t → s is also consistent (prevents many-to-one conflicts).

mapping_st = {}
mapping_ts = {}


⸻

✅ Step 3: Loop Through Both Strings Together

Use zip(s, t) to loop over characters in s and t at the same time.

for char_s, char_t in zip(s, t):


⸻

✅ Step 4: Apply Mapping Rules
	1.	Forward Mapping Check (s → t):
	•	If char_s is already in mapping_st, ensure it maps to the same char_t.
	•	If not, store the mapping.
	2.	Reverse Mapping Check (t → s):
	•	If char_t is already in mapping_ts, ensure it maps to the same char_s.
	•	If not, store the mapping.

    if char_s in mapping_st:
        if mapping_st[char_s] != char_t:
            return False
    else:
        mapping_st[char_s] = char_t

    if char_t in mapping_ts:
        if mapping_ts[char_t] != char_s:
            return False
    else:
        mapping_ts[char_t] = char_s


⸻

✅ Step 5: If All Characters Pass, Return True

If the loop completes without returning False, the strings are isomorphic.

return True
⸻

🧠 Why Two Dictionaries?

Because:
	•	s → t should be unique: 'a' → 'x', not 'a' → 'x' and 'a' → 'y'.
	•	t → s should also be unique: 'x' → 'a', not 'x' → 'a' and 'x' → 'b'.

So, we prevent:
	•	One-to-many and many-to-one mappings.

⸻

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