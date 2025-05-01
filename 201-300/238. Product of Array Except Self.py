"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
"""
Your code is an optimized solution to the “Product of Array Except Self” problem. It smartly avoids using extra arrays for prefix and postfix, keeping space complexity at O(1) (excluding the output array). Let’s walk through how it works:

⸻

✅ Goal:

Given an array nums, return an array answer such that:

answer[i] = product of all elements in nums except nums[i]

Without using division, and in O(n) time.

⸻

🔧 Step-by-Step Logic:

l = len(nums)
answer = [1] * l

	•	answer is initialized to all 1s.
	•	This will eventually store the final product for each index.

⸻

🔁 First Pass: Left to Right (Prefix Product)

prefix = 1
for i in range(l):
    answer[i] = prefix
    prefix *= nums[i]

	•	For each index i, you store the product of all elements before i.
	•	The variable prefix accumulates the product of elements from the start up to i-1.

Example with nums = [1,2,3,4]:

i	prefix	answer[i]	prefix after update
0	1	1	1×1 = 1
1	1	1	1×2 = 2
2	2	2	2×3 = 6
3	6	6	6×4 = 24

So after this loop, answer = [1, 1, 2, 6]
(Each answer[i] = product of all elements to the left of i)

⸻

🔁 Second Pass: Right to Left (Postfix Product)

postfix = 1
for i in reversed(range(l)):
    answer[i] *= postfix
    postfix *= nums[i]

	•	Now, you multiply each answer[i] with the product of all elements after i
	•	The variable postfix accumulates the product from end to start.

Continuing the example:

i	postfix	answer[i] (before)	answer[i] (after)	postfix after update
3	1	6	6×1 = 6	1×4 = 4
2	4	2	2×4 = 8	4×3 = 12
1	12	1	1×12 = 12	12×2 = 24
0	24	1	1×24 = 24	24×1 = 24

Now answer = [24, 12, 8, 6] ✅

⸻

📌 Final Output:

For input nums = [1, 2, 3, 4], output is:

[24, 12, 8, 6]

Which is correct, because:
	•	24 = 2×3×4
	•	12 = 1×3×4
	•	8 = 1×2×4
	•	6 = 1×2×3

⸻

🚀 Summary of Technique:
	1.	First pass: Store prefix products in answer.
	2.	Second pass: Multiply with postfix products.
	3.	Space-efficient: No need for extra arrays; O(1) extra space (excluding output).


"""
from typing import  List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l = len(nums)
        answer = [1]*l
        prefix = 1
        for i in range(l):
            answer[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in reversed(range(l)):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer

slo = Solution()

nums = [1,2,3,4]
print(nums)

print(slo.productExceptSelf(nums))


"""
        prefix = 1
        postfix = 1
        l = len(nums)
        prefix_arr = []
        postfix_arr = [0]*l
        answer = [0]*l
        for x in nums:
            prefix_arr.append(prefix * x)
            prefix *= x
        for i in reversed(range(l)):
            postfix_arr[i]=(postfix * nums[i])
            postfix *= nums[i]

        answer[0]=postfix_arr[1]
        answer[l-1]=prefix_arr[-2]

        for i in range(1,l-1):
            answer[i] = (prefix_arr[i-1]*postfix_arr[i+1])
"""