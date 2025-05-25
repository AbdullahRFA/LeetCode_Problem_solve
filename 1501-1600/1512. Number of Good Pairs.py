"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.



Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0

"""
"""
✅ 1. Hashing / Frequency Count (Using dict or collections.Counter)
	•	Why: You need to count how many times each number appears, and use that count to compute how many good pairs can be formed.
	•	How: If a number appears freq times, the number of good pairs it contributes is:
\text{pairs} = \frac{freq \times (freq - 1)}{2}
(This is combinatorics: choosing 2 indices out of freq identical elements.)
"""
from collections import Counter

def numIdenticalPairs(nums):
    freq = Counter(nums)
    count = 0
    for v in freq.values():
        count += v * (v - 1) // 2
    return count

# 🎯 User input example
if __name__ == "__main__":
    nums = list(map(int, input("Enter array elements: ").split()))
    print("Number of good pairs:", numIdenticalPairs(nums))