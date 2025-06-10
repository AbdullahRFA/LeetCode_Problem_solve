"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.


Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false



Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.strip().split()
        pattern = list(pattern)
        if len(s_list)!=len(pattern):
            return False
        print(len(s_list))
        print(len(pattern))
        p_char = {}
        s_word = {}
        for char , word in zip(pattern,s_list):
            if char in p_char:
               if p_char[char] != word:
                return False
            p_char[char] = word

            if word in s_word:
                if s_word[word] != char:
                    return False
            s_word[word] = char
        return True


slv = Solution()
pattern = "abba"
s = "dog cat cat fish"
print(slv.wordPattern(pattern,s))