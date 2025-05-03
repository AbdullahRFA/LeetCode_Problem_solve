"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

"""
"""
    ✅ Solution Technique Used

You’re using the Mathematical Sum Formula approach:

Step-by-step Explanation:
	1.	Understand the expected sum:
	•	If no number were missing, then the array would contain all numbers from 0 to n.
	•	The sum of first n natural numbers is:
\text{expected\_sum} = \frac{n(n+1)}{2}
	2.	Get the actual sum:
	•	Use Python’s sum(nums) to calculate the total of elements currently in the list.
	3.	Subtract to find the missing number:
	•	The difference between the expected sum and the actual sum gives the missing number.
"""

from typing import  List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = (n*(n+1))//2
        actual_sum = sum(nums)
        return expected_sum-actual_sum


sl = Solution()
nums = [3,0,1]
print(sl.missingNumber(nums))

"""
n = len(nums)
        num =[x for x in range(n)]
        for x in num:
            if x not in nums:
                return x
"""