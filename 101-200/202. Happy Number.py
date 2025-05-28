"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
"""
"""
💡 What is a Happy Number?

A number is happy if:
	1.	You replace it with the sum of the squares of its digits.
	2.	You repeat this process.
	3.	If you eventually reach 1, it’s a happy number.
	4.	If it falls into a loop (i.e., you keep seeing the same number), it’s not happy.

⸻

🔍 How to Solve It?

We simulate the process:
	1.	Use a set to keep track of all numbers we have already seen.
	2.	For each number:
	•	Replace it with the sum of the squares of its digits.
	•	If this number is already in the set → ❌ loop detected → return False.
	•	If it becomes 1 → ✅ return True.

⸻

🔧 Steps (Algorithm)
	1.	Initialize an empty set seen.
	2.	While n is not 1:
	•	If n is already in seen, return False (we’re in a loop).
	•	Add n to seen.
	•	Replace n with the sum of the squares of its digits.
	3.	If n becomes 1, return True.

⸻

🧠 Why This Works
	•	All unhappy numbers eventually fall into a known cycle.
	•	All happy numbers reach 1 and stop.
	•	Using a set prevents infinite loops.

⸻

🔄 Example

Input: n = 19

Process:

19 → 1² + 9² = 82
82 → 8² + 2² = 68
68 → 6² + 8² = 100
100 → 1² + 0² + 0² = 1 ✅


⸻

⏱ Time & Space Complexity
	•	Time Complexity: O(log n) per iteration (processing digits), but total steps are limited due to the cycle length.
	•	Space Complexity: O(log n) for the set (storing seen numbers).

"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            # Calculate sum of squares of digits
            n = sum(int(digit) ** 2 for digit in str(n))

        return True

# Test input
slv = Solution()
n = int(input("Enter a number: "))
print(slv.isHappy(n))