class Solution:
    def asteroidCollision(self, nums):
        n = len(nums)
        stack = []
        for i in range(n):
            if nums[i]>=0:
                stack.append(nums[i])
            else:
                while stack and stack[-1]>0 and stack[-1]<abs(nums[i]):
                    stack.pop()
                if  stack and stack[-1]==abs(nums[i]):
                    stack.pop()
                    continue
                    
                if not stack or stack[-1]<0:
                    stack.append(nums[i])
        return stack

slv = Solution()
nums = list(map(int, input("Enter the list of numbers: ").split(" ")))
print(slv.asteroidCollision(nums))

# 4 7 1 1 2 -3 -7 17 15 -16