"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.



Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

"""
ugly_number = []
def prime_factor():
    for x in range(1,100000000):
        tem=x
        for p in [2,3,5]:
            while x%p == 0:
                x//=p
        if x==1:
            ugly_number.append(tem)

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        prime_factor()
        # print(ugly_number)
        print(len(ugly_number))
        return ugly_number[n-1]
slv = Solution()
n = 1690
print(slv.nthUglyNumber(n))