"""
Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.



Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.
"""
"""
📘 Explanation
	1.	Filter Even Numbers: Get only the even numbers using list comprehension.
	2.	No Even Case: Return -1 if the list is empty.
	3.	Count Frequencies: Use Counter to count how often each even number appears.
	4.	Sorting Criteria:
	•	Sort by descending frequency: -x[1]
	•	If tie, sort by ascending value: x[0]
	5.	Return Result: The first element of the sorted list is the answer.

⸻

📦 Example Walkthrough

For nums = [0,1,2,2,4,4,1]:
	•	Even numbers → [0,2,2,4,4]
	•	Frequencies → Counter({2: 2, 4: 2, 0: 1})
	•	Sorted → [(2, 2), (4, 2), (0, 1)]
	•	✅ Output: 2 (tie between 2 and 4; pick smaller)

⸻

⏱ Time & Space Complexity
	•	Time Complexity: O(n log n) due to sorting (worst-case all elements are even)
	•	Space Complexity: O(n) for storing filtered even numbers and the Counter
"""
from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        # Filter only even numbers
        even_nums = [num for num in nums if num % 2 == 0]

        # If no even numbers, return -1
        if not even_nums:
            return -1

        # Count frequencies of even numbers
        count = Counter(even_nums)

        # Sort by frequency (descending), then by value (ascending)
        most_frequent = sorted(count.items(), key=lambda x: (-x[1], x[0]))

        # Return the number with highest frequency (and smallest if tied)
        return most_frequent[0][0]
slv = Solution()
nums = [0,1,2,2,4,4,1]
print(slv.mostFrequentEven(nums))