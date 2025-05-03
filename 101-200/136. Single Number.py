"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1



"""

"""
✅ Technique: Bitwise XOR

🔧 XOR Properties:
	1.	a ^ a = 0 → any number XORed with itself is zero.
	2.	a ^ 0 = a → any number XORed with 0 stays unchanged.
	3.	XOR is commutative and associative:
	•	So, the order doesn’t matter.
	
	•	Initially, res = 0
	•	For each number in the list:
	•	It XORs the number with res.
	•	Duplicate numbers cancel each other (since a ^ a = 0)
	•	The number that appears once remains at the end.
	
	📌 Use This Technique When:
	•	Every number appears twice, except one that appears once.
"""
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0;
        for num in nums:
            res ^= num
        return  res



slv = Solution()
print(slv.singleNumber([1,2,2,3,3,4,4]))

"""
✅ Technique Summary:
	•	This approach uses a hash map (dictionary) to count frequencies.
	•	It’s simple and works well even if more than one number has different frequencies.
	
        fre = {}
        for x in nums:
            fre[x] = fre.get(x,0)+1
        for k,v in fre.items():
            if v == 1:
                return k
"""
