"""
Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits.



Example 1:

Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.
Example 2:

Input: num = 30
Output: 14
Explanation:
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.

"""
"""
🧠 Solution Technique Explained:
	1.	Loop through each number from 1 to num:
	    •	You’re examining every number in this range.
	2.	Convert the number to a string:
	    •	This allows you to iterate over each digit easily.
	3.	Use a generator expression:
	    sum(int(d) for d in str(x))
	        •	This calculates the sum of the digits of number x.

	4.	Check if the digit sum is even:
	    •	Use sum % 2 == 0 to verify evenness.
	5.	Count it:
	    •	If the digit sum is even, increase the counter.
"""
class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for x in range(1, num + 1):
            SumOf_X = sum(int(d) for d in str(x))  # Calculate digit sum
            if SumOf_X % 2 == 0:  # Check if it's even
                count += 1
        return count


# === Take user input and test ===
slv = Solution()
num = int(input("Enter a positive number: "))
result = slv.countEven(num)
print("Count of numbers with even digit sums:", result)