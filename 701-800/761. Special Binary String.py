'''
761. Special Binary String
You are given a string s of length n containing only zeros and ones. Convert s into a special binary string. A binary string is special if it satisfies the following conditions:
- The number of 0's is equal to the number of 1's.
- Every prefix of the binary string has at least as many 1's as 0's.
You can perform the following operation on the string any number of times:
- Choose two consecutive, non-empty, special substrings of s, and swap them.
Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.
Example 1:
Input: s = "11011000"
Output: "11100100"
Explanation: The strings "10" and "1100" are special substrings, and when swapped, the string becomes "11100100", which is the lexicographically largest string possible.   
Example 2:
Input: s = "10"
Output: "10" 

Intuition:
To solve the problem, we can use a recursive approach to identify and sort the special binary substrings. The idea is to break down the string into its special substrings, sort them in reverse order (to get the lexicographically largest result), and then concatenate them back together.

Approach:
1. Define a recursive function that takes a string s as input.
2. If the length of s is less than or equal to 2, return s as it is already a special binary string.
3. Initialize a variable `start` to keep track of the starting index of the current special substring, a variable `count` to keep track of the balance between 1's and 0's, and an empty list `parts` to store the special substrings.
4. Iterate through the string s using a for loop:
   - For each character, update the `count` variable: increment it for '1' and decrement it for '0'.
   - When `count` reaches 0, it indicates that we have found a special substring. Extract the substring from `start` to the current index, recursively call the function on the middle part of the substring (excluding the outer '1' and '0'), and append the result to the `parts` list. Update `start` to the next index.
5. After the loop, sort the `parts` list in reverse order to get the lexicographically largest arrangement of the special substrings.
6. Join the sorted parts and return the resulting string.

Time Complexity: O(n^2), where n is the length of the input string s.   
Space Complexity: O(n), where n is the length of the input string s.



'''


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        
        start = 0
        count  = 0
        parts = []

        for i, char in enumerate(s):
            if char == "1":
                count +=1
            else:
                count -= 1
            
            if count == 0:
                middle = self.makeLargestSpecial(s[start+1:i])
                parts.append("1"+middle+"0")
                start = i + 1
        
        parts.sort(reverse = True)
        return "".join(parts)