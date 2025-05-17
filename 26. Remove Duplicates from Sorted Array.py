"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""
"""
📘 Explanation of the Solution Technique

🔍 Goal:

Remove duplicates from a sorted/unsorted list in-place, and return the count of unique elements (k), while modifying the original list so that the first k elements are the unique values.

🧠 Technique:
	•	Set for tracking seen elements:
        We use a set called seen to store already encountered elements.
	•	Two pointers (i, j):
	•	i iterates through the original list.
	•	j tracks the position to write the next unique value.
	•	Overwrite duplicates:
        When we find a new unique element, we write it to index j and increment j.

🕒 Time Complexity:
	•	O(n), where n is the length of the input list.

💾 Space Complexity:
	•	O(k), where k is the number of unique elements (space used by the set).
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(set(nums))  # Count of unique elements
        j = 0
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[j] = nums[i]  # Overwrite the duplicate
                j += 1
                seen.add(nums[i])
        return k

# -------------------
# Input from the user
input_str = input("Enter the list of integers (space-separated): ")
nums = list(map(int, input_str.strip().split()))

# Object and method call
sol = Solution()
k = sol.removeDuplicates(nums)

# Output
print("Number of unique elements:", k)
print("List after removing duplicates:", nums[:k])