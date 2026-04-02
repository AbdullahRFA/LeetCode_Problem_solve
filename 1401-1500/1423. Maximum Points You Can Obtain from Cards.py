from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        result = 0
        left = 0 
        right = len(cardPoints)-1
        left_sum = right_sum = 0

        if k == len(cardPoints):
            return sum(cardPoints)
        left_sum = sum(cardPoints[0:k])
        result = left_sum
        for i in range(k-1,-1,-1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[right]
            right -= 1
            result = max(result,left_sum+right_sum)
        return result