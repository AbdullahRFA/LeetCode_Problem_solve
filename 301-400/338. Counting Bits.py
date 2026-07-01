'''
338. Counting Bits
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
Example 1:  
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
Constraints:
0 <= n <= 10^5

Intuition:
To solve the problem, we can iterate through all numbers from 0 to n and count the number of 1's in their binary representation. We can use Python's built-in `bin()` function to convert a number to its binary representation and then use the `count()` method to count the number of 1's.

Approach:
1. Initialize an array `res` of size n + 1 with all elements set to 0.
2. Iterate through all numbers from 0 to n:
   - For each number i, convert it to its binary representation using `bin(i)`.
   - Count the number of 1's in the binary representation using the `count("1")` method.
   - Store the count in the `res` array at index i.
   
Time Complexity: O(n * log(n)), where n is the input integer. The log(n) factor comes from the time taken to convert a number to its binary representation.

Space Complexity: O(n), where n is the input integer, as we are using an additional array `res` of size n + 1 to store the results. 

'''


# from typing import List


# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         res = [0]*(n+1)

#         for i in range(n+1):
#             bin_rep = bin(i)
#             cnt = bin_rep.count("1")
#             res[i]=cnt
#         return res
    
    
# Solution 2

'''
338. Counting Bits
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1 
2 --> 10
Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
Constraints:
0 <= n <= 10^5

Intuition:
To solve the problem, we can use dynamic programming to build the result array iteratively. The key observation is that the number of 1's in the binary representation of a number i can be derived from the number of 1's in the binary representation of i // 2 (i right-shifted by 1) plus the least significant bit (i & 1). This allows us to compute the result for each number based on previously computed results.

Approach:
1. Initialize an array `res` of size n + 1 with all elements set to 0.
2. Iterate through all numbers from 1 to n:
   - For each number i, compute the number of 1's in its binary representation using the formula:
     res[i] = res[i >> 1] + (i & 1)
   - Here, `i >> 1` gives us the number obtained by removing the least significant bit of i, and `i & 1` checks if the least significant bit is 1 (which contributes to the count of 1's).
3. Return the `res` array as the final result.
'''


from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)

        for i in range(1, n+1):
            res[i] = res[i>>1] + (i&1)
        return res
    
    
    
'''

⸻

Intuition

A brute-force approach would be to convert every number from 0 to n into its binary representation and count the number of 1s. However, this would take O(n log n) time because each number has up to log n bits.

Instead, we observe a pattern:

* If we right shift a number by one bit (i >> 1), we remove its last binary digit.
* The number of 1s in i is therefore equal to:
    * the number of 1s in i >> 1, plus
    * 1 if the last bit is 1, otherwise 0.

The last bit can be obtained using:

i & 1

Thus, we get the recurrence:

bits(i) = bits(i >> 1) + (i & 1)

Since i >> 1 is always smaller than i, its answer has already been computed. This allows us to build the answer using Dynamic Programming in a single pass.

⸻

Approach

1. Create an array res of size n + 1 initialized with 0.
2. Iterate from 1 to n.
3. For each number i:
    * Compute i >> 1 to remove the last bit.
    * Compute i & 1 to determine whether the last bit is 1.
    * Use the recurrence:

res[i] = res[i >> 1] + (i & 1)

4. Return the res array.

⸻

Algorithm

1. Initialize res = [0] * (n + 1).
2. For every i from 1 to n:
    * Find the number of set bits of i >> 1.
    * Add 1 if the last bit of i is set.
    * Store the result in res[i].
3. Return res.

⸻

Complexity Analysis

* Time Complexity: O(n)
    * We process each number exactly once, and each computation takes constant time.
* Space Complexity: O(n)
    * An array of size n + 1 is used to store the answers.

⸻

Code

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res

This explanation is suitable for LeetCode’s Intuition, Approach, Complexity, and Code sections.

'''
