from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # maxi = 0
        # # ones = 0

        # for i in range(n):
        #     ones = 0
        #     zeros = 0
        #     for j in range(i,n):
        #         if nums[j] == 1:
        #             ones += 1
        #             maxi = max(maxi, ones)
        #         else:
        #             zeros += 1
        #             if zeros <= k:
        #                 ones += 1
        #                 maxi = max(maxi, ones)
        #             else:
        #                 break

        n = len(nums)
        maxi=left=right=zeros=0

        while right<n:
            if nums[right] == 0:
                zeros += 1
            while zeros>k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            maxi = max(maxi, right-left+1)
            right += 1
        return maxi

        return maxi
            




