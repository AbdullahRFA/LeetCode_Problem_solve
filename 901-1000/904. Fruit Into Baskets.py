from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        maxi = 0

        # O(N**2)

        # for i in range(n):
        #     myset=set()
        #     for j in range(i,n):
        #         myset.add(fruits[j])
        #         if len(myset)<3:
        #             maxi=max(maxi,j-i+1)
        #         else:
        #             break
            # return maxi


        # O(2N)

        # left=right=0
        # mydict = {}
        # while right < n:
        #     mydict[fruits[right]]=mydict.get(fruits[right],0)+1
        #     while len(mydict)>2:
        #         mydict[fruits[left]]-=1
        #         if mydict[fruits[left]] == 0:
        #             del mydict[fruits[left]]
        #         left+=1
        #     if len(mydict)<3:
        #         maxi = max(maxi,right-left+1)
        #     right += 1
        # return maxi


        # O(N)
        left=right=0
        mydict = {}
        while right < n:
            mydict[fruits[right]]=mydict.get(fruits[right],0)+1
            if len(mydict)>2:
                mydict[fruits[left]]-=1
                if mydict[fruits[left]] == 0:
                    del mydict[fruits[left]]
                left+=1
            if len(mydict)<3:
                maxi = max(maxi,right-left+1)
            right += 1
        return maxi
