from ast import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        res2 = [-1]*n
        stack = []

        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack:
                res2[i]= stack[-1]
            stack.append(nums2[i])
        
        mapGreater = {}

        for i in range(n):
            mapGreater[nums2[i]]=res2[i]
        n2 = len(nums1)
        ans=[-1]*n2

        for i in range(n2):
            ans[i]=mapGreater[nums1[i]]

        return ans
        