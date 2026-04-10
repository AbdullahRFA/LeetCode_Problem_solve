'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]
Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

Solution: Hash Map
1. We can use a hash map (dictionary) to group the anagrams together.
2. We iterate through each string in the input array `strs`, and for each string, we sort the characters in the string to create a key. Anagrams will have the same sorted key.
3. We then append the original string to the list of anagrams corresponding to that sorted key in the hash map.
4. Finally, we return the values of the hash map, which will be lists of anagrams.  

Time Complexity: O(n * k log k), where n is the number of strings in the input array and k is the maximum length of a string, since we need to sort each string.
Space Complexity: O(n * k), since in the worst case, all strings could be anagrams of each other and we would need to store all of them in the hash map.

'''

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ang = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            ang[key].append(word)
        return list(ang.values())
        