"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


💡 Step-by-Step Thinking

We want to find the lowest price to buy and the highest profit we can get afterward by selling.

⸻

🧠 Intuition:

Loop through the list:
	•	Keep track of the minimum price so far (best day to buy).
	•	On each day, calculate the profit if you sold today: today's price - min_price_so_far.
	•	Track the maximum profit we’ve seen so far.



"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')  # Start with infinity so any price will be lower
        max_profit = 0          # Initialize max profit to 0

        for price in prices:
            if price < min_val:
                min_val = price  # Found a new lower buying price
            else:
                profit = price - min_val  # Calculate potential profit
                max_profit = max(profit, max_profit)  # Update max profit if it's higher

        return max_profit


# Example usage
sol = Solution()

# Example 1
prices1 = [7, 1, 5, 3, 6, 4]
print("Max Profit (Example 1):", sol.maxProfit(prices1))  # Output: 5

# Example 2
prices2 = [7, 6, 4, 3, 1]
print("Max Profit (Example 2):", sol.maxProfit(prices2))  # Output: 0