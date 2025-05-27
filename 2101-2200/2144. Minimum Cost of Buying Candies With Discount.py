"""
A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.

The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or equal to the minimum cost of the two candies bought.

For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3, they can take the candy with cost 1 for free, but not the candy with cost 4.
Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of buying all the candies.



Example 1:

Input: cost = [1,2,3]
Output: 5
Explanation: We buy the candies with costs 2 and 3, and take the candy with cost 1 for free.
The total cost of buying all candies is 2 + 3 = 5. This is the only way we can buy the candies.
Note that we cannot buy candies with costs 1 and 3, and then take the candy with cost 2 for free.
The cost of the free candy has to be less than or equal to the minimum cost of the purchased candies.
Example 2:

Input: cost = [6,5,7,9,2,2]
Output: 23
Explanation: The way in which we can get the minimum cost is described below:
- Buy candies with costs 9 and 7
- Take the candy with cost 6 for free
- We buy candies with costs 5 and 2
- Take the last remaining candy with cost 2 for free
Hence, the minimum cost to buy all candies is 9 + 7 + 5 + 2 = 23.
Example 3:

Input: cost = [5,5]
Output: 10
Explanation: Since there are only 2 candies, we buy both of them. There is not a third candy we can take for free.
Hence, the minimum cost to buy all candies is 5 + 5 = 10.

"""
"""
🔹 Step-by-step:
	1.	Sort the cost array in ascending order.
	2.	Start buying candies from the most expensive end (i.e., right to left).
	3.	For every 3rd candy (i.e., positions 3rd, 6th, 9th from the end), skip it (because it’s free).
	4.	Add the other candies to the total cost.

This approach ensures the free candy is always the cheapest among every three, which gives the maximum saving.

Input:
Enter the costs of the candies (space-separated): 6 5 7 9 2 2

Output:
✅ Minimum total cost to buy all candies with offer: 24

Explanation:
Sorted: [2, 2, 5, 6, 7, 9]
From back:
Buy 9, 7 -> Pay
Skip 6 -> Free
Buy 5, 2 -> Pay
Skip 2 -> Free

Total = 9 + 7 + 5 + 2 = 23
"""
from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        mncost = 0
        for i in range(1, len(cost) + 1):
            if i % 3 != 0:
                mncost += cost[-i]  # Buying the two most expensive, skipping every 3rd
        return mncost


# --------------------------
# 🎯 User Input Handling
# --------------------------
if __name__ == "__main__":
    cost = list(map(int, input("Enter the costs of the candies (space-separated): ").split()))

    sol = Solution()
    result = sol.minimumCost(cost)
    print("✅ Minimum total cost to buy all candies with offer:", result)