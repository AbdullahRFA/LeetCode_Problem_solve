'''
788. Rotated Digits
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.    
Each digit must be rotated - we cannot choose to leave it alone.
A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
Given a positive integer N, return the number of good numbers between 1 and N inclusive.
Example 1:
Input: N = 10
Output: 4
Explanation: There are four good numbers in the range [1, 10]: 2, 5, 6, 9.
Example 2:  
Input: N = 100
Output: 40
Explanation: There are 40 good numbers in the range [1, 100]: 2, 5, 6, 9, 12, 15, 16, 19, 21, 22, 25, 26, 29, 51, 52, 55, 56, 59, 61, 62, 65, 66, 69, 81, 82, 85, 86, 89, 91, 92, 95, 96, 99.
Example 3:
Input: N = 10000
Output: 2324
Explanation: There are 2324 good numbers in the range [1, 10000].   

Constraints:
1 <= N <= 10000 

Intuition:
1. We can solve this problem by iterating through all the numbers from 1 to N and checking if each number is a good number. To check if a number is a good number, we can convert it to a string and iterate through each character (digit) in the string. We will maintain two sets: one for valid digits that can be rotated to form a different digit (2, 5, 6, 9) and another for invalid digits that cannot be rotated to form any valid digit (3, 4, 7). If we encounter an invalid digit, we can immediately conclude that the number is not a good number. If we encounter a valid digit, we will set a flag to indicate that the number has at least one valid digit that can be rotated to form a different digit. After checking all the digits, if the number is valid and has at least one valid digit, we will increment our count of good numbers.

Approach:
1. We will initialize a count variable to keep track of the number of good numbers. We will also define two sets: one for valid digits (good) and another for invalid digits (invalid).
2. We will iterate through all the numbers from 1 to N inclusive. For each number, we will convert it to a string and check each digit.
3. We will maintain two flags: one to indicate if the number is valid (valid) and another to indicate if the number has at least one valid digit that can be rotated to form a different digit (change).
4. For each digit in the number, we will check if it is in the good set or the invalid set. If it is in the good set, we will set the change flag to True. If it is in the invalid set, we will set the valid flag to False and break out of the loop since we already know the number is not a good number.
5. After checking all the digits, if the number is valid and has at least one valid digit that can be rotated to form a different digit, we will increment our count of good numbers.
6. Finally, we will return the count of good numbers as the final answer.

Time Complexity: O(N * D), where N is the input number and D is the number of digits in the largest number (which is log10(N)). We will need to iterate through all the numbers from 1 to N, and for each number, we will need to check each digit, which takes O(D) time.
Space Complexity: O(1), since we are using a constant amount of space to store the sets of valid and invalid digits, as well as a few variables to keep track of the count and flags. We are not using any additional data structures that grow with the input size.        


'''


class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = True
        change = False
        good = {2,5,6,9}
        invalid = {3,4,7}
        cnt = 0

        for num in range(1,n+1):
            valid = True
            change = False

            for ch in str(num):
                digit = int(ch)
                if digit in good:
                    change = True
                elif digit in invalid:
                    valid = False
                    break
            if valid and change:
                cnt+=1

        return cnt
                
            