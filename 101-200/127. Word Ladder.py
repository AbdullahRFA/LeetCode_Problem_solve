'''
127. Word Ladder
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.
Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation.
Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
All the words in wordList are unique.

Solution: BFS
1. We can use a breadth-first search (BFS) approach to solve this problem. We will start from the beginWord and explore all possible transformations by changing one letter at a time.  
2. We will use a queue to keep track of the current word and the level (or depth) of the transformation. We will also use a set to keep track of the words in the wordList for O(1) lookups.
3. We will initialize the queue with the beginWord and a level of 1. We will then enter a while loop that continues until the queue is empty. Inside the loop, we will pop the front element of the queue, which gives us the current word and its level. If the current word is the endWord, we will return the level as the length of the transformation sequence.
4. If the current word is not the endWord, we will generate all possible transformations by changing each letter of the current word to every other letter in the alphabet. For each generated word, if it is in the wordList set, we will add it to the queue with a level incremented by 1 and remove it from the wordList set to avoid processing it again.
5. If we exhaust the queue without finding the endWord, we will return 0 to indicate that no valid transformation sequence exists.

Time Complexity: O(N * M^2), where N is the number of words in the wordList and M is the length of each word. This is because for each word, we are generating M possible transformations by changing each letter, and for each transformation, we are checking if it exists in the wordList set.
Space Complexity: O(N), where N is the number of words in the wordList, due to the queue and the set used for storing the words. In the worst case, we may need to store all the words in the queue if they are all one letter different from each other.
'''


from ast import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque()
        queue.append((beginWord,1))

        while queue:
            curr_word, level = queue.popleft()
            if curr_word == endWord:
                return level
            
            for i in range(len(curr_word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == curr_word[i]:
                        continue
                    
                    new_word = curr_word[:i] + ch + curr_word[i+1:]

                    if new_word in wordSet:
                        queue.append((new_word, level+1))
                        wordSet.remove(new_word)
        return 0