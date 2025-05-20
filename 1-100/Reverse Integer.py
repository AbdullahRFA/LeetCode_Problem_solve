"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        tem = abs(x)
        reverse_number = 0
        while tem != 0:
            nm = tem%10
            reverse_number = reverse_number*10 + nm
            tem //= 10
        # print(reverse_number)
        reverse_number = int(reverse_number)*sign
        if reverse_number < -2**31 or reverse_number > 2**31-1:
            return 0
        return reverse_number





slv = Solution()
t = int(input())
for _ in range(t):
    num = int(input())
    print(slv.reverse(num))

