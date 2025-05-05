"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tem_s = []
        for x in s:
            if x.isalnum():               # keep only alphanumeric
                tem_s.append(x.lower())   # convert to lowercase
        tem_s = "".join(tem_s)            # join list to form cleaned string
        print(tem_s)                      # (for debugging)
        print(tem_s[::-1])                # reversed string (for debugging)
        return tem_s == tem_s[::-1]       # check palindrome


slv = Solution()
# s = "A man, a plan, a canal: Panama"
s = '0P'
print(slv.isPalindrome(s))