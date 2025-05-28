"""
An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.

Given an integer n, return true if n is an ugly number.



Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors.
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

"""
"""
	1.	We divide n by 2, 3, and 5 as much as possible.
	2.	If after removing all these factors, n == 1, then it’s ugly.
	3.	If any other prime factors remain (i.e., n > 1), it’s not ugly.
"""
class Solution:
    def isUgly(self, n: int) -> bool:
        # prime_factor = []
        # if n == 1 or n == 0:
        #     return True
        # res = (1,2,3,5)
        # while n%2 ==0 :
        #     prime_factor.append(2)
        #     n//=2
        # while n%3 ==0 :
        #     prime_factor.append(3)
        #     n//=3
        # while n%5 ==0 :
        #     prime_factor.append(5)
        #     n//=5
        # prime_factor.append(n)
        # prime_factor = set(prime_factor)
        # # print(prime_factor,n)
        # return prime_factor.issubset(res)
        if n <= 0:
            return False
        for p in [2,3,5]:
            while n%p == 0:
                n//=p
        return n == 1

slv = Solution()
n = 1
print(slv.isUgly(n))