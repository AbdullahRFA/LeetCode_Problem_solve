'''
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
Constraints:
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.
Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9, and you want to check one by one to see ift has its subsequence. In this scenario, how would you change your code?


Solution: Two Pointers
1. We can use two pointers to check if s is a subsequence of t.
2. We initialize two pointers, `l` and `r`, to 0, which will be used to traverse the strings s and t, respectively.
3. We also initialize a variable `cnt` to keep track of the number of characters in s that we have matched in t.    
4. We enter a while loop that continues as long as `l` is less than the length of s and `r` is less than the length of t.
5. Inside the loop, we check if the characters at the current positions of s and t (i.e., `s[l]` and `t[r]`) are the same. If they are, it means we have found a match for the current character in s, so we increment the `cnt` variable and move the pointer `l` to the next character in s.
6. Regardless of whether we found a match or not, we move the pointer `r` to the next character in t to continue searching for the next character in s.
7. After the loop, we check if the value of `cnt` is equal to the length of s. If it is, it means we have found all characters of s in t in the correct order, so we return `True`. Otherwise, we return `False`.

Time Complexity: O(n), where n is the length of string t, since we may need to traverse the entire string t in the worst case.
Space Complexity: O(1), since we are using only a constant amount of extra space for the pointers and the counter variable.
'''



from collections import Counter
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        l = r =0
        n = len(s)
        m = len(t)
        cnt = 0
        while l< n and r< m:
            if s[l] == t[r]:
                cnt += 1
                l +=1
            r+=1
        return n==cnt
