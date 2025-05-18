"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
"""
🧠 Solution Technique

Problem: Given an integer array nums and an integer k, return the k most frequent elements.

⸻

✅ Step-by-Step Breakdown
	1.	Use Counter:
	•	Count how many times each number appears.
	•	Example: Counter([1,1,1,2,2,3]) → {1:3, 2:2, 3:1}
	2.	Sort Dictionary Items:
	•	Sort by frequency in descending order using:
	    sorted(dct.items(), key=lambda item: -item[1])
		3.	Pick Top k Elements:
	•	After sorting, select the first k items’ keys from the sorted list.

⸻

🕒 Time and Space Complexity
	•	Time Complexity:
	•	Counting: O(n)
	•	Sorting: O(n log n)
	•	Overall: O(n log n)
	•	Space Complexity:
	•	Counter + Output List → O(n)
"""
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count frequency using Counter
        dct = Counter(nums)

        # Step 2: Sort the items by frequency in descending order
        dct = sorted(dct.items(), key=lambda item: -item[1])

        # Step 3: Collect the top k frequent elements
        res = []
        for i in range(k):
            res.append(dct[i][0])
        return res


# --------------------------
# 🎯 User Input Handling
# --------------------------
if __name__ == "__main__":
    # Get input list
    nums = list(map(int, input("Enter the list of numbers (space separated): ").split()))

    # Get value of k
    k = int(input("Enter the value of k (top k frequent elements to return): "))

    # Create Solution object and call the method
    sol = Solution()
    result = sol.topKFrequent(nums, k)

    # Print the result
    print("Top", k, "frequent elements:", result)