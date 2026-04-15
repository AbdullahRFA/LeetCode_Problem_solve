'''
80. Remove Duplicates from Sorted Array II
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).
Constraints:
1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


Solution: Two Pointers
1. We can use a two-pointer approach to solve this problem in-place. We will maintain two pointers, `i` and `j`, where `i` will keep track of the position where we will place the next unique element, and `j` will iterate through the array to find the unique elements.
2. We will start both pointers at index 2, since the first two elements can always be kept as they are.
3. We will iterate through the array with pointer `j` starting from index 2. For each element at index `j`, we will compare it with the element at index `i-2`. If they are not equal, it means that the element at index `j` is a unique element that can be placed at index `i`. We will assign `nums[i] = nums[j]` and increment `i` by 1.
4. If the element at index `j` is equal to the element at index `i-2`, it means that we have already seen this element twice, and we will skip it by not incrementing `i`.
5. After the loop, `i` will be the length of the modified array with at most two occurrences of each unique element. We will return `i` as the result.  

Time Complexity: O(n), where n is the length of the input array, since we iterate through the array once.
Space Complexity: O(1), since we are modifying the array in-place and not using any extra space for another array.
'''

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums)<=2:
            return len(nums)
        
        i = 2

        for j in range(2,len(nums)):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i+=1
        return i