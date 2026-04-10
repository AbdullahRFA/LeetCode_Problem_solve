'''
167. Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
Constraints:    
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution.

Solution: Hash Map
1. We can use a hash map (dictionary) to store the numbers we have seen so far and their corresponding indices.
2. We iterate through the `numbers` array using a for loop, and for each number, we calculate the complement by subtracting the current number from the target.
3. If the complement is already in the hash map, we have found our two numbers and return their indices (adding 1 to each since the problem uses 1-indexing).
4. Otherwise, we store the current number and its index in the hash map.

Time Complexity: O(n), where n is the length of the `numbers` array, since we may need to iterate through the entire array in the worst case.
Space Complexity: O(n), since we may need to store all the numbers in the hash map in the worst case.

Solution: Two Pointers
1. Since the `numbers` array is already sorted, we can use the two-pointer technique to find the two numbers that add up to the target.
2. We initialize two pointers, `l` and `r`, to the beginning and end of the array, respectively.
3. We enter a while loop that continues as long as `l` is less than `r`.
4. Inside the loop, we calculate the sum of the numbers at the two pointers. If the sum is equal to the target, we have found our two numbers and return their indices (adding 1 to each since the problem uses 1-indexing).
5. If the sum is greater than the target, it means we need to decrease the sum, so we move the right pointer `r` one step to the left.
6. If the sum is less than the target, it means we need to increase the sum, so we move the left pointer `l` one step to the right.

Time Complexity: O(n), where n is the length of the `numbers` array, since we may need to iterate through the entire array in the worst case.
Space Complexity: O(1), since we are using only a constant amount of extra space for the two pointers and the variables to store the sum and target.
'''


from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # dct = {}

        # for i in range(len(numbers)):
        #     if (target-numbers[i]) in dct:
        #         return dct[(target-numbers[i])]+1,i+1
        #     else:
        #         dct[numbers[i]]=i
                
                
        l = 0
        r = len(numbers)-1

        while r>l:
            if numbers[l]+numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l]+numbers[r] > target:
                r -=1
            elif numbers[l]+numbers[r] < target:
                l +=1
        