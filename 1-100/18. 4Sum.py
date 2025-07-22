"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""
from  typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # n = len(nums)
        # my_set = set()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             for l in range(k+1,n):
        #                 Sum = nums[i] + nums[j] + nums[k] +nums[l]
        #                 if Sum == target:
        #                     temp = [nums[i] , nums[j] , nums[k] ,nums[l]]
        #                     temp.sort()
        #                     my_set.add(tuple(temp))
        # return [list(x) for x in my_set]

        # n = len(nums)
        # my_set = set()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         seen = set()
        #         for k in range(j+1,n):
        #             fourth = target-(nums[i] + nums[j] + nums[k])
        #             if fourth in seen:
        #                 temp = [nums[i] , nums[j] , nums[k], fourth]
        #                 temp.sort()
        #                 my_set.add(tuple(temp))

        #             seen.add(nums[k])
        # return [list(x) for x in my_set]

        n = len(nums)
        nums.sort()
        # my_set = set()
        res = []
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue

                k = j+1
                l = n-1

                while k<l:
                    Sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if Sum == target:
                        # my_set.add(tuple([nums[i] , nums[j] ,nums[k] ,nums[l]]))
                        res.append([nums[i] , nums[j] ,nums[k] ,nums[l]])
                        k+=1
                        l-=1

                        while k<l and nums[k] == nums[k-1]:
                            k+=1
                        while k<l and nums[l] == nums[l+1]:
                            l-=1
                    elif Sum < target:
                        k+=1
                    else:
                        l-=1
        # return [list(x) for x in my_set]
        return res

slv = Solution()

nums = [2,2,2,2,2]
target = 8
print(slv.fourSum(nums,target))