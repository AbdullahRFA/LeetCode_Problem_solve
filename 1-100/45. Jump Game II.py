'''
45. Jump Game II
Given an array of non-negative integers nums, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
Return the minimum number of jumps you need to reach the last index.
The test cases are generated such that you can reach the last index.
Solution: Greedy
1. We can keep track of the current range of indices we can jump to, and the farthest index we can reach within that range.
2. We initialize three variables: jmp to keep track of the number of jumps, left to keep track of the left boundary of the current range, and right to keep track of the right boundary of the current range.
3. We iterate through the array until we reach the last index. For each index within the current range (from left to right), we calculate the farthest index we can reach by taking the maximum of the current farthest index and the sum of the current index and the jump length at that index.
4. After iterating through the current range, we update the left boundary to be one more than the right boundary, and the right boundary to be the farthest index we can reach. We also increment the jump count by 1.
5. We repeat this process until we reach the last index, at which point we return the jump count.
'''


from ast import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jmp = 0
        left = 0
        right =0

        while right < len(nums)-1:
            farthest = 0
            for i in range(left, right+1):
                farthest = max(farthest, nums[i]+i)
            left = right + 1
            right = farthest
            jmp += 1
        return jmp
                
        