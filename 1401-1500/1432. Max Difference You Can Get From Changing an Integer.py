"""
You are given an integer num. You will apply the following steps to num two separate times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). Note y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
Let a and b be the two results from applying the operation to num independently.

Return the max difference between a and b.

Note that neither a nor b may have any leading zeros, and must not be 0.



Example 1:

Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888
Example 2:

Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8


Constraints:

1 <= num <= 108
"""
"""
🔍 Step-by-Step Solution Technique:

🧠 Goal:

Replace all occurrences of one digit with another digit only once to:
	•	Maximize the number.
	•	Minimize the number.

⸻

🔄 Step-by-Step for num = 11891:

🔹 Step 1: Maximize
	•	Convert 11891 to string → "11891"
	•	First non-9 digit is '1'
	•	Replace all '1' with '9' → "99899" → max_number = 99899

🔹 Step 2: Minimize
	•	First digit is '1', so we cannot replace it with '1'
	•	Look at other digits:
	•	At index 2: '8' is not '0' and not equal to '1'
	•	Replace all '8' with '0' → "11091" → min_number = 11091

🔹 Step 3: Difference
	•	99899 - 11091 = 88808
"""
class Solution:
    def maxDiff(self, num: int) -> int:
        temp = str(num)

        # Step 1: Find max_number by replacing first non-9 digit with 9
        for x in temp:
            if x != '9':
                max_number = int(temp.replace(x, '9'))
                break
        else:
            max_number = num  # All digits are already 9

        # Step 2: Find min_number
        if temp[0] != '1':
            # Replace the first digit with '1'
            min_number = int(temp.replace(temp[0], '1'))
        else:
            # Replace the first non-zero digit that isn't equal to the first with '0'
            for i in range(1, len(temp)):
                if temp[i] != '0' and temp[i] != temp[0]:
                    min_number = int(temp.replace(temp[i], '0'))
                    break
            else:
                min_number = num  # All digits already '1' or '0'

        # Step 3: Return the difference
        return max_number - min_number


# === User Input ===
num = int(input("Enter a number: "))
slv = Solution()
result = slv.maxDiff(num)
print("Maximum Difference:", result)