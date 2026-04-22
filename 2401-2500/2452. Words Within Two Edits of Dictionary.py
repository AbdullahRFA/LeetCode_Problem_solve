'''
2452. Words Within Two Edits of Dictionary
You are given two string arrays, queries and dictionary, where queries[i] is a word you want to search for, and dictionary is a list of available words. Return a list of all words in queries that are within two edits of any word in dictionary.
A word is within two edits of another word if you can insert, delete, or replace a character in the other word at most two times to make them equal.
Example 1:
Input: queries = ["word","note","ants","wood"], dictionary = ["wood","jord","moat"]
Output: ["word","note","wood"]
Explanation:
- "word" can be edited to "wood" by replacing the 'r' with 'o'.
- "note" can be edited to "moat" by replacing the 'n' with 'm' and the 'e' with 'a'.
- "ants" cannot be edited to any word in dictionary with at most two edits.
- "wood" can be edited to "wood" with zero edits.
Example 2:  
Input: queries = ["yes"], dictionary = ["not"]
Output: []
Explanation: "yes" cannot be edited to "not" with at most two edits.
Constraints:
1 <= queries.length, dictionary.length <= 100
1 <= queries[i].length, dictionary[j].length <= 100
queries[i] and dictionary[j] consist of lowercase English letters.  

Solution: Brute Force
intuition: We can use a brute-force approach to solve this problem. We will iterate through each word in the queries array and compare it with each word in the dictionary array. For each pair of words, we will count the number of edits (insertions, deletions, or replacements) required to make the two words equal. If the number of edits is less than or equal to 2, we will add the query word to the result list and break out of the inner loop to move on to the next query word. To count the number of edits between two words, we can use a simple loop to compare the characters of the two words. We will keep track of the number of differences between the two words. If the lengths of the two words are different, we can also account for the extra characters as edits. If the total number of edits exceeds 2, we can break out of the loop early to optimize the performance.

Approach:
1. Initialize an empty list `res` to store the result.
2. Iterate through each word `q` in the `queries` array.
3. For each word `q`, iterate through each word `d` in the `dictionary` array.
4. Initialize a variable `diff` to count the number of edits required to make `q` and `d` equal.
5. Use a loop to compare the characters of `q` and `d`. For each pair of characters, if they are different, increment the `diff` variable.
6. If the lengths of `q` and `d` are different, account for the extra characters as edits by adding the absolute difference of their lengths to `diff`.
7. If `diff` is less than or equal to 2, add `q` to the result list `res` and break out of the inner loop to move on to the next query word.
8. After iterating through all query words, return the result list `res`.   

Time Complexity: O(Q * D * L), where Q is the number of query words, D is the number of dictionary words, and L is the maximum length of the words. We will compare each query word with each dictionary word, and for each comparison, we will check up to L characters.
Space Complexity: O(Q), where Q is the number of query words. In the worst case, all query words could be within two edits of the dictionary words, and we would store all query words in the result list.

'''


from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []

        for q in queries:
            for d in dictionary:
                diff = 0

                for a, b in zip(q, d):
                    if a != b:
                        diff += 1
                        if diff > 2:
                            break

                if diff <= 2:
                    res.append(q)
                    break

        return res
    
    
    
    # class Solution:
    # def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
    #     res = []

    #     for q in queries:
    #         for d in dictionary:
    #             i,j,c=0,0,0
    #             while i< len(d):
    #                 if q[i]!=d[j]:
    #                     c+=1
    #                 i+=1
    #                 j+=1
    #             if c<=2:
    #                 res.append(q)
    #                 break

    #     return res