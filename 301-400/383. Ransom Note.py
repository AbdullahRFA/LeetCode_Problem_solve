'''
383. Ransom Note    
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise. Each letter in magazine can only be used once in ransomNote.
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
Constraints:
1 <= ransomNote.length, magazine.length <= 10^5
ransomNote and magazine consist of lowercase English letters.
Follow up: What if the ransomNote and magazine strings contain upper-case letters? Would your solution still work? How would you adapt your solution to such a case?

Solution: Hash Map
1. We can use a hash map (dictionary) to count the occurrences of each character in the magazine string.
2. We iterate through the magazine string and update the count of each character in the hash map.
3. We then iterate through the ransomNote string and check if each character is available in the hash map with a count greater than 0. If it is, we decrement the count of that character in the hash map. If it is not available or the count is 0, it means we cannot construct the ransomNote from the magazine, so we return False.
4. If we successfully check all characters in the ransomNote, it means we can construct the ransomNote from the magazine, so we return True.


Time Complexity: O(n + m), where n is the length of the magazine string and m is the length of the ransomNote string, since we need to iterate through both strings.
Space Complexity: O(1), since the hash map will at most contain 26 entries for lowercase English letters, which is a constant amount of space.
'''


from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mg = Counter(list(magazine))
        for x in ransomNote:
            if x in mg:
                mg[x]-=1
                if mg[x] == 0:
                    del mg[x]
            else:
                return False
        return True
        