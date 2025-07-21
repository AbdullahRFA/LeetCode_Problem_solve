"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

"""
from typing import  List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # my_set = set()
        res = []
        n = len(nums)
        # Brute force solution O(N^3)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 temp = [nums[i], nums[j], nums[k]]
        #                 temp.sort()
        #                 my_set.add(tuple(temp))
        # ans = [list(x) for x in my_set]
        # return ans

        # Better Solution O(N^2)
        # for i in range(n):
        #     seen = set()
        #     for j in range(i+1,n):
        #         third = -(nums[i]+nums[j])
        #         if third in seen:
        #             temp =[nums[i],nums[j],third]
        #             temp.sort()
        #             my_set.add(tuple(temp))
        #         seen.add(nums[j])
        # res = [list(x) for x in my_set]
        # return res

        # Optimal Solution
        nums.sort()
        for i in range(n):
            if i!=0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = n-1

            while j<k:
                Triplet_sum = nums[i] + nums[j] + nums[k]
                if Triplet_sum < 0:
                    j+=1
                elif Triplet_sum > 0:
                    k-=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1

                    while j<k and nums[j] == nums[j-1]:
                            j+=1
                    while j<k and nums[k]==nums[k+1]:
                            k-=1
        return res

slv = Solution()
nums = [-1,0,1,2,-1,-4]
print(slv.threeSum(nums))


"""

⸻

🔍 Problem Recap:

Find all unique triplets in the array that sum to 0.

Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

⸻

✅ Method 1: Brute Force (O(n³))

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if nums[i] + nums[j] + nums[k] == 0:
                temp = [nums[i], nums[j], nums[k]]
                temp.sort()
                my_set.add(tuple(temp))

🔧 Mechanism:
	•	Try all combinations of 3 elements.
	•	If they sum to 0, store the sorted tuple in a set to avoid duplicates.
	•	Finally, convert the set of tuples back to a list of lists.

⏱ Time Complexity:
	•	O(n³): Three nested loops.

🧠 Space Complexity:
	•	O(k): Where k is the number of unique triplets (used in the set).
	•	Also uses O(1) extra variables.

⸻

⚡ Method 2: Better Using Hashing (O(n²))

for i in range(n):
    seen = set()
    for j in range(i+1, n):
        third = -(nums[i] + nums[j])
        if third in seen:
            temp = [nums[i], nums[j], third]
            temp.sort()
            my_set.add(tuple(temp))
        seen.add(nums[j])

🔧 Mechanism:
	•	Fix one element (nums[i]).
	•	For every pair with the fixed element, check if the complement (-(nums[i]+nums[j])) exists in the set.
	•	This mimics the 2Sum problem.
	•	Store sorted tuples in a set to avoid duplicates.

⏱ Time Complexity:
	•	O(n²): Two loops and set operations are O(1) on average.

🧠 Space Complexity:
	•	O(n) for the seen set.
	•	O(k) for storing the final triplets in the set.

⸻

💎 Method 3: Optimal Two-Pointer (O(n²))

nums.sort()
for i in range(n):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    j = i + 1
    k = n - 1
    while j < k:
        sum = nums[i] + nums[j] + nums[k]
        if sum < 0:
            j += 1
        elif sum > 0:
            k -= 1
        else:
            res.append([nums[i], nums[j], nums[k]])
            j += 1
            k -= 1
            while j < k and nums[j] == nums[j-1]:
                j += 1
            while j < k and nums[k] == nums[k+1]:
                k -= 1

🔧 Mechanism:
	•	Sort the array first.
	•	Fix one element (nums[i]) and use two pointers (j, k) to find the other two elements.
	•	Skip duplicates to avoid repeated triplets.
	•	This method avoids extra space for hashing or set.

⏱ Time Complexity:
	•	O(n²): Outer loop runs n times, inner two-pointer search runs O(n) in total.
	•	Sorting takes O(n log n).

🧠 Space Complexity:
	•	O(1) auxiliary space (excluding the result list).

⸻

🆚 Summary Comparison:

Method	        Time Complexity	        Space Complexity	        Deduplication	            Use Case
Brute Force	        O(n³)	                O(k)	                    With Set	    Simple to implement, inefficient
Hashing	            O(n²)	                O(n + k)	                With Set	    Better, but still extra space
Two Pointers	    O(n²)	                O(1)	                    In-place skip	✅ Optimal solution


⸻

"""