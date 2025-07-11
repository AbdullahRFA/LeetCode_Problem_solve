"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"



Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)  # Convert to list to allow modification
        i, j = 0, len(s) - 1
        # print(vowels)
        while i < j:
            # Move i forward until vowel found
            while i < j and s[i] not in vowels:
                i += 1
            # Move j backward until vowel found
            while i < j and s[j] not in vowels:
                j -= 1

            # Swap the vowels
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return ''.join(s)
sol = Solution()
print(sol.reverseVowels("IceCreAm"))  # Output: "AceCreIm"