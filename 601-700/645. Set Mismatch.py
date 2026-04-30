"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.



Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]

Intuition:
1. We can solve this problem by using the input array itself to keep track of the numbers that we have seen. We can iterate through the input array and for each number, we can mark the index corresponding to that number as negative. If we encounter a number that has already been marked as negative, then that number is the duplicate. After we have marked all the numbers, we can iterate through the input array again and find the index that is still positive, which will be the missing number.

Approach:
1. We will initialize two variables, dup_num and miss_num, to store the duplicate number and the missing number, respectively.
2. We will iterate through the input array nums and for each number, we will calculate the index corresponding to that number by taking the absolute value of the number and subtracting 1 from it. We will then check if the number at that index is negative. If it is negative, then that means we have already seen that number before, and we will set dup_num to the absolute value of the current number. If it is not negative, then we will mark that index as negative by negating the number at that index.
3. After we have marked all the numbers, we will iterate through the input array again and find the index that is still positive. The index of the positive number will be the missing number, and we will set miss_num to that index plus 1 (since the numbers are from 1 to n).
4. Finally, we will return the duplicate number and the missing number in the form of an array.

Time Complexity: O(n), where n is the number of elements in the input array. We will need to iterate through the input array twice, which takes O(n) time.
Space Complexity: O(1), since we are using only a constant amount of extra space to store the duplicate number and the missing number, and we are modifying the input array in place to keep track of the numbers that we have seen. In the worst case, if the input array is already sorted, we may not need to use any extra space at all.

for another Solution:

Intuition:
1. We can also solve this problem by using a hash map (or a Counter) to count the occurrences of each number in the input array. We can then iterate through the hash map to find the number that occurs twice and the number that is missing.

Approach:
1. We will use a Counter to count the occurrences of each number in the input array nums.
2. We will then iterate through the items in the Counter and check for the number that occurs twice (i.e., the number with a count of 2) and the number that is missing (i.e., the number that is not present in the Counter).
3. Finally, we will return the duplicate number and the missing number in the form of an array.

Time Complexity: O(n), where n is the number of elements in the input array. We will need to iterate through the input array to count the occurrences of each number, which takes O(n) time. We will also need to iterate through the items in the Counter, which takes O(n) time in the worst case.
Space Complexity: O(n), since we are using a Counter to store the occurrences of each number in the input array. In the worst case, if all the numbers in the input array are unique, we will need to store all n numbers in the Counter, which takes O(n) space.

"""

# from typing import List


# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         dup_num = 0
#         miss_num = 0
#         n = len(nums)
#         for i in range(n):
#             index = abs(nums[i])-1
#             if nums[index]<0:
#                 dup_num = abs(nums[i])
#             else:
#                 nums[index]=-nums[index]
#         for i in range(n):
#             if nums[i]>0:
#                 miss_num = i+1
#         return [dup_num, miss_num]


from typing import List
from collections import  Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dct = Counter(nums)

        n = len(nums)

        for k, v in dct.items():
            if v == 2:
                twice_num = k
                break
        for i in range(1, n + 1):
            if i not in dct:
                missing_number = i
                break
        return [twice_num, missing_number]
slv = Solution()
nums = [1,2,2,4]
print(slv.findErrorNums(nums))

