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
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]*n
        it2=it3=it5=0

        for i in range(1,n):
            next2 = ugly_numbers[it2]*2
            next3 = ugly_numbers[it3]*3
            next5 = ugly_numbers[it5]*5

            next = min(next2,next3,next5)

            ugly_numbers[i]=next

            if next == next2:
                it2+=1
            if next == next3:
                it3+=1
            if next == next5:
                it5+=1
        return ugly_numbers[-1]
slv = Solution()
n = 1690
print(slv.nthUglyNumber(n))