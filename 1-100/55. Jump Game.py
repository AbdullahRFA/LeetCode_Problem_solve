'''
55. Jump Game
Given an array of non-negative integers nums, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
Solution: Greedy
1. We can keep track of the maximum index we can reach at any point in time.
2. We iterate through the array, and for each index, we check if it is greater than the maximum index we can reach. If it is, then we cannot reach this index and we return false.
3. If it is not, we update the maximum index we can reach by taking the maximum of the current maximum index and the sum of the current index and the jump length at that index.
4. If we successfully iterate through the array without returning false, it means we can reach the last index, and we return true at the end.
'''


from ast import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0

        for i in range(len(nums)):
            if i > max_index:
                return False
            max_index = max(max_index, i+nums[i])

        return True