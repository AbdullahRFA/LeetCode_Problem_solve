import heapq
def k_smallest(nums, k):
    heapq.heapify(nums)
    print(nums)
    return [heapq.heappop(nums) for _ in range(k)]

print(k_smallest([9, 4, 7, 1, -2, 6, 5], 3))  # [-2, 1, 4]