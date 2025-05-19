"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.



Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
"""
"""
✅ Solution Technique: Character Frequency Intersection

💡 Idea:
	1.	Count the frequency of each character in the first word using Counter.
	2.	For each remaining word, update the frequency count by intersecting it with the current counter using the & operator.
	3.	The final counter contains only the characters that appear in all words, with the correct number of duplicates.
	4.	Expand the counter into a list of characters.

Metric
Complexity
Time
O(n * k), where n = number of words, k = average word length
Space
O(1) since only lowercase letters are used (aâ€“z)

"""
from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Start with the counter of the first word
        common = Counter(words[0])

        # Intersect with counters of the remaining words
        for word in words[1:]:
            common &= Counter(word)

        # Expand the characters based on their count
        res = []
        for char, freq in common.items():
            res.extend([char] * freq)
        return res


# 🎯 Test the solution
svl = Solution()

print(svl.commonChars(["bella", "label", "roller"]))  # Output: ['e', 'l', 'l']
print(svl.commonChars(["cool", "lock", "cook"]))  # Output: ['c', 'o']