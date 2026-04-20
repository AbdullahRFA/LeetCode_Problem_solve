'''
126. Word Ladder II
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
Example 1:  
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation.
Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
All the words in wordList are unique.

Solution: BFS + DFS
1. We can use a breadth-first search (BFS) approach to find the shortest transformation sequences. We will start from the beginWord and explore all possible transformations by changing one letter at a time. We will use a queue to keep track of the current word and the level (or depth) of the transformation. We will also use a set to keep track of the words in the wordList for O(1) lookups.
2. We will initialize the queue with the beginWord and a level of 1. We will then enter a while loop that continues until the queue is empty. Inside the loop, we will pop the front element of the queue, which gives us the current word and its level. If the current word is the endWord, we will set a flag to indicate that we have found the endWord and break out of the loop.
3. If the current word is not the endWord, we will generate all possible transformations by changing each letter of the current word to every other letter in the alphabet. For each generated word, if it is in the wordList set, we will add it to the queue with a level incremented by 1 and remove it from the wordList set to avoid processing it again. We will also keep track of the parent-child relationships between the words in a dictionary, where the key is the child word and the value is a list of parent words that can transform into the child word.
4. After the BFS is complete, we will have a dictionary of parent-child relationships that we can use to reconstruct the shortest transformation sequences. We will use a depth-first search (DFS) approach to traverse the parent-child relationships and build the transformation sequences. We will start from the endWord and recursively visit its parents until we reach the beginWord, building the path along the way. We will reverse the path at the end to get the correct order of the transformation sequence.
5. Finally, we will return the list of all the shortest transformation sequences.

Time Complexity: O(N * M * 26 + N * M), where N is the number of words in the wordList, M is the length of each word, and 26 is the number of letters in the English alphabet. The BFS step takes O(N * M * 26) time to generate all possible transformations for each word in the wordList, and the DFS step takes O(N * M) time to reconstruct the transformation sequences.

Space Complexity: O(N * M), where N is the number of words in the wordList and M is the length of each word, due to the queue, the set used for storing the words, and the dictionary used for storing the parent-child relationships. In the worst case, we may need to store all the words in the queue and the parent-child relationships for all the words in the wordList.
'''


from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        parents = defaultdict(list)
        level = {beginWord}
        found = False
        
        while level and not found:
            next_level = set()
            wordSet -= level   
            
            for word in level:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + ch + word[i+1:]
                        
                        if new_word in wordSet:
                            parents[new_word].append(word)
                            next_level.add(new_word)
                            
                            if new_word == endWord:
                                found = True
            
            level = next_level
        

        res = []
        
        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            
            for parent in parents[word]:
                dfs(parent, path + [parent])
        
        if found:
            dfs(endWord, [endWord])
        
        return res