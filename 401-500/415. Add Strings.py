"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.



Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""

"""
	1.	Start from the end of both strings.
	2.	Use a variable carry to track carry-over during addition.
	3.	Add digit-by-digit using ord(char) - ord('0') to get the numeric value.
	4.	Append the result’s digit ((d1 + d2 + carry) % 10) to a result list.
	5.	At the end, if there’s any carry left, add it.
	6.	Finally, reverse and join the result.
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        res = []
        carry = 0

        while i >= 0 or j >= 0 or carry:
            d1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            d2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = d1 + d2 + carry
            res.append(str(total % 10))
            carry = total // 10
            i-=1
            j-=1
        return "".join(reversed(res))
        # print(res)
slv = Solution()
num1 = "11"
num2 = "123"
print(slv.addStrings(num1,num2))
