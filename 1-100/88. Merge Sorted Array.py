"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""
"""
🧠 Solution Technique (In-place Merge of Two Sorted Arrays)

Problem Statement Recap:
	•	nums1 has a size of m + n, with the first m elements being valid and the last n elements being placeholders (0) to hold elements from nums2.
	•	nums2 contains n sorted elements.
	•	You must merge nums2 into nums1 in-place so that the result is sorted.

⸻

⚙️ How It Works (Current Solution):
	1.	Overwrite the placeholder 0s in nums1:
	•	Place elements of nums2 starting from index m of nums1.
	2.	Sort the combined list:
	•	Use Python’s built-in sort() to sort nums1 after merging.

🔧 Note: While this approach uses sort(), which is not truly optimal, it satisfies the in-place merge constraint and works well in interviews unless O(n) time is specifically required.

⸻

🕒 Time and Space Complexity:
	•	Time Complexity: O((m + n) log(m + n)) due to the sorting step.
	•	Space Complexity: O(1) extra space (modifies nums1 in-place).
"""
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges nums2 into nums1 in-place assuming nums1 has enough space.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]  # Replace the trailing zero with nums2 element
        nums1.sort()  # Sort the combined list

# ---- Main Function for User Input ----
if __name__ == "__main__":
    nums1 = list(map(int, input("Enter nums1 with extra 0s (space separated): ").strip().split()))
    m = int(input("Enter number of actual elements in nums1 (m): "))

    nums2 = list(map(int, input("Enter nums2 (space separated): ").strip().split()))
    n = len(nums2)

    # Pad nums1 with zeros if not padded already
    while len(nums1) < m + n:
        nums1.append(0)

    solution = Solution()
    solution.merge(nums1, m, nums2, n)

    print("Merged nums1:", nums1)