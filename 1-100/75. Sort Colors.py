class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        n = len(nums)
        right = n-1

        current = 0

        while current <= right:
            if nums[current] == 0:
                nums[left],nums[current] = nums[current],nums[left]
                left+=1
                current+=1
                # print(nums)
            elif nums[current] == 1:
                current+=1
                # print(nums)
            else:
                nums[right],nums[current] = nums[current],nums[right]
                right-=1
                # print(nums)



        