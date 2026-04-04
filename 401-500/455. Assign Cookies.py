from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0
        n = len(g)
        m = len(s)
        l=r =0
        while l<n and r < m:
            if s[r]>= g[l]:
                cnt+=1
                r +=1
                l+=1
            else:
                r+=1
        return cnt