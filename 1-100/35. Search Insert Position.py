"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

"""
"""
Goal:
Find the index of a target value in a sorted list of distinct integers. If it’s not present, return the index where it should be inserted to maintain order.

⸻

⚙️ Algorithm Steps:
	1.	Initialize two pointers:
	•	left = 0 (start of array)
	•	right = len(nums) - 1 (end of array)
	2.	Binary search loop:
	•	While left <= right, do:
	•	mid = (left + right) // 2
	•	If nums[mid] == target: return mid
	•	If nums[mid] > target: search in the left half → right = mid - 1
	•	If nums[mid] < target: search in the right half → left = mid + 1
	3.	When loop ends, target isn’t found. left will be the correct insertion index.

⸻

⏱️ Time & Space Complexity:
	•	Time Complexity: O(log n)
Because the array is divided in half each iteration (binary search).
	•	Space Complexity: O(1)
No extra space used.
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


# User input section
if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted array (space-separated): ").strip().split()))
    target = int(input("Enter target value: "))

    sol = Solution()
    index = sol.searchInsert(nums, target)

    print(f"Target should be at index: {index}")