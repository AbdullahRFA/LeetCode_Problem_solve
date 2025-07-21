"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104

"""
from typing import  List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = []
        closest_sum = float('inf')
        for i in range(n-2):
            j = i+1
            k = n-1

            while j<k:
                current_sum = nums[i] + nums[j] + nums[k]

                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                if current_sum < target:
                    j+=1
                elif current_sum > target:
                    k-=1
                else:
                    return closest_sum
        return closest_sum
nums = [-1,2,1,-4]
target = 1
slv = Solution()
print(slv.threeSumClosest(nums,target))

"""
⸻

✅ Solution Technique: Two Pointers + Sorting

Steps:
	1.	Sort the array to use two-pointer technique effectively.
	2.	Iterate through the array with index i, treating nums[i] as the first number.
	3.	Set two pointers:
        •	left = i + 1
        •	right = n - 1
	4.	For each triplet (nums[i], nums[left], nums[right]):
        •	Calculate the sum: curr_sum = nums[i] + nums[left] + nums[right]
        •	If this is closer to the target than our previous best, update the closest.
        •	Move left or right based on whether curr_sum is less or more than target.
	5.	Return the closest sum after checking all triplets.

⸻


✅ Time and Space Complexity
	•	Time Complexity: O(n^2)
	•	Sorting takes O(n log n)
	•	Outer loop runs n times, inner while loop runs in total O(n) across all iterations.
	•	Space Complexity: O(1)
	•	No extra space except variables.

⸻

✅ Example Walkthrough:

Input: nums = [-1, 2, 1, -4], target = 1
Sorted: [-4, -1, 1, 2]
	•	Try i = 0 → nums[i] = -4, left = 1, right = 3
	•	sum = -4 + (-1) + 2 = -3 → closer than inf
	•	Try i = 1 → nums[i] = -1, left = 2, right = 3
	•	sum = -1 + 1 + 2 = 2 → closer to 1 than -3

Closest sum found is 2.

⸻

"""