'''

860. Lemonade Change

1. You are given an integer array bills where bills[i] is the bill the ith customer pays. You have an infinite number of 5, 10, and 20 dollar bills.
2. You need to provide the correct change to each customer such that the net transaction is that the customer pays 5 dollars.
3. Note that the first customer pays with a bill and does not receive change.
4. Return true if you can provide every customer with the correct change, or false otherwise.

Solution: Greedy
 1. If the customer pays with a 5 dollar bill, we just need to increase the count of 5 dollar bills.
 2. If the customer pays with a 10 dollar bill, we need to check if we have at least one 5 dollar bill to give change. If we do, we decrease the count of 5 dollar bills and increase the count of 10 dollar bills. If we don't, we return false.
 3. If the customer pays with a 20 dollar bill, we have two options to give change: we can give one 10 dollar bill and one 5 dollar bill, or we can give three 5 dollar bills. We prefer to give one 10 dollar bill and one 5 dollar bill if we have them, because it preserves more 5 dollar bills for future customers. If we don't have a 10 dollar bill, we check if we have at least three 5 dollar bills to give change. If we do, we decrease the count of 5 dollar bills by three. If we don't, we return false.
 4. If we successfully give change to all customers, we return true at the end.

'''


from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        five = 0
        ten = 0

        for note in bills:
            if note == 5:
                five += 1
            elif note == 10:
                if five >= 1:
                    five -= 1
                    ten+=1
                else:
                    return False
            else:
                if five >=1 and ten>=1:
                    five -=1
                    ten -=1
                elif five>=3:
                    five -= 3
                else:
                    return False
        return True
        