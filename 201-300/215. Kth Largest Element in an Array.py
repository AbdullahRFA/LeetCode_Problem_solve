"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
"""

⸻

✅ Problem Statement

Given an integer array nums and an integer k, return the kth largest element in the array.

⸻

🎯 Solution Technique: Using Min-Heap (Priority Queue)

💡 Idea:
	•	We maintain a min-heap of size k.
	•	This heap always contains the k largest elements seen so far.
	•	The smallest among these k elements (which is at the top of the min-heap) is the kth largest in the full array.

⸻

🧠 Step-by-Step Explanation:

Step 1: Create an empty min-heap

min_heap = []

This will store the top k largest elements in ascending order.

⸻

Step 2: Push every number into the heap

heapq.heappush(min_heap, num)

Push current number to the heap.

⸻

Step 3: Maintain only k elements in the heap

if len(min_heap) > k:
    heapq.heappop(min_heap)

	•	If heap grows larger than k, remove the smallest element.
	•	This keeps only the k largest elements in the heap.

⸻

Step 4: Return the kth largest element

return min_heap[0]

	•	Now, the smallest element in the heap of size k is the kth largest overall.

⸻

🕒 Time Complexity:
	•	Each heappush and heappop operation takes O(log k).
	•	You do this n times for n elements.
	•	Total Time: O(n log k)

⸻

✅ Why Heap is Better Here?
	•	Using sort() would be O(n log n).
	•	With a heap, we do better for large arrays when k is much smaller than n.

⸻

🧪 Example:

Input:

nums = [3,2,1,5,6,4], k = 2

Heap building:
	•	Add 3 → [3]
	•	Add 2 → [2, 3]
	•	Add 1 → pop 1 → [2, 3]
	•	Add 5 → pop 2 → [3, 5]
	•	Add 6 → pop 3 → [5, 6]
	•	Add 4 → pop 4 → [5, 6]

Now heap[0] = 5, which is the 2nd largest element.

⸻

"""
import heapq


def findKthLargest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort(reverse=True)
#         return nums[k-1]


# --------------------------
# 🎯 User Input
# --------------------------
if __name__ == "__main__":
    nums = list(map(int, input("Enter the list of numbers (space separated): ").split()))
    k = int(input("Enter the value of k (to find the kth largest element): "))

    result = findKthLargest(nums, k)
    print(f"The {k}th largest element is:", result)