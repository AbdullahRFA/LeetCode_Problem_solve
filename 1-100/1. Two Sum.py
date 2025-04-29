class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in idx:
                return [idx[y],i]
            idx[x]=i