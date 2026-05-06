


import heapq
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        seen = {1}

        for _ in range(n):
            curr = heapq.heappop(heap)

            for p in primes:
                new_val = p*curr
                if new_val not in seen:
                    seen.add(new_val)
                    heapq.heappush(heap, new_val)
        return curr