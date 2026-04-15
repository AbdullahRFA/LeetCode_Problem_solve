
'''
209. Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
Constraints:
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

Solution: Two Pointers
1. We can use a two-pointer approach to solve this problem efficiently. We will maintain two pointers, `l` and `r`, which will represent the left and right boundaries of the current subarray we are considering.
2. We will also maintain a variable `total` to keep track of the sum of the current subarray. We will initialize `l` to 0, `total` to 0, and `min_len` to infinity to keep track of the minimum length of the subarray that meets the condition.
3. We will iterate through the array with the right pointer `r` from 0 to n-1. For each element at index `r`, we will add it to `total`.
4. After adding the element at index `r` to `total`, we will check if `total` is greater than or equal to `target`. If it is, we will update `min_len` with the minimum of its current value and the length of the current subarray (which is `r - l + 1`). We will then subtract the element at index `l` from `total` and move the left pointer `l` to the right by incrementing it by 1. We will repeat this process until `total` is less than `target`.
5. After the loop, if `min_len` is still infinity, it means we did not find any subarray that meets the condition, and we will return 0. Otherwise, we will return `min_len` as the result.

Time Complexity: O(n), where n is the length of the input array, since we iterate through the array once with the right pointer and each element is processed at most twice (once when added to `total` and once when subtracted from `total`).
Space Complexity: O(1), since we are using only a constant amount of extra space for the variables.

'''


from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len( nums)
        l = 0
        total = 0
        min_len = float('inf')

        for r in range(n):
            total+=nums[r]

            while total>=target:
                min_len = min(min_len, r-l+1)
                total-=nums[l]
                l+=1
        
        return 0 if min_len == float('inf') else min_len