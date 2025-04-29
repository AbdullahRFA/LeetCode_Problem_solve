class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in idx:
                return [idx[y],i]
            idx[x]=i



"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
⸻

🔢 Example:

nums = [3, 2, 4]
target = 6



⸻

✅ Goal:

Find two numbers in nums that add up to 6, and return their indices.

⸻

🧠 Step-by-Step Execution:

We start with an empty hash map (num_map = {}) and loop through nums using enumerate().

⸻

🔁 1st iteration:
	•	i = 0
	•	num = 3
	•	complement = 6 - 3 = 3
	•	Check: Is 3 in num_map? → ❌ No
	•	Action: Store 3 with its index → num_map = {3: 0}

⸻

🔁 2nd iteration:
	•	i = 1
	•	num = 2
	•	complement = 6 - 2 = 4
	•	Check: Is 4 in num_map? → ❌ No
	•	Action: Store 2 with its index → num_map = {3: 0, 2: 1}

⸻

🔁 3rd iteration:
	•	i = 2
	•	num = 4
	•	complement = 6 - 4 = 2
	•	Check: Is 2 in num_map? → ✅ Yes (num_map[2] = 1)
	•	🎯 Match found!
	•	Return: [1, 2]

⸻

✅ Final Output:

[1, 2]

Because nums[1] + nums[2] = 2 + 4 = 6

⸻

Would you like me to walk through the [3, 3], target = 6 case next?
"""