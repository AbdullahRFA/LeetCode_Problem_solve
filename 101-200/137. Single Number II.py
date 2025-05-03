from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        fre = {}
        for x in nums:
            fre[x] = fre.get(x,0)+1
        for k,v in fre.items():
            if v == 1:
                return k



slv = Solution()
print(slv.singleNumber([1,2,2,3,3,4,4]))