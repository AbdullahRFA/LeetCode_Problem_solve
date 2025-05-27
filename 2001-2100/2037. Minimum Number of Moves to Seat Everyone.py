"""
There are n availabe seats and n students standing in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student.

You may perform the following move any number of times:

Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

Note that there may be multiple seats or students in the same position at the beginning.



Example 1:

Input: seats = [3,1,5], students = [2,7,4]
Output: 4
Explanation: The students are moved as follows:
- The first student is moved from position 2 to position 1 using 1 move.
- The second student is moved from position 7 to position 5 using 2 moves.
- The third student is moved from position 4 to position 3 using 1 move.
In total, 1 + 2 + 1 = 4 moves were used.
Example 2:

Input: seats = [4,1,5,9], students = [1,3,2,6]
Output: 7
Explanation: The students are moved as follows:
- The first student is not moved.
- The second student is moved from position 3 to position 4 using 1 move.
- The third student is moved from position 2 to position 5 using 3 moves.
- The fourth student is moved from position 6 to position 9 using 3 moves.
In total, 0 + 1 + 3 + 3 = 7 moves were used.
Example 3:

Input: seats = [2,2,6,6], students = [1,3,2,6]
Output: 4
Explanation: Note that there are two seats at position 2 and two seats at position 6.
The students are moved as follows:
- The first student is moved from position 1 to position 2 using 1 move.
- The second student is moved from position 3 to position 6 using 3 moves.
- The third student is not moved.
- The fourth student is not moved.
In total, 1 + 3 + 0 + 0 = 4 moves were used.
"""
"""

💡 Solution Technique

Problem Statement:
Given positions of seats and students, return the minimum number of total moves required so that every student sits on a seat.
A move is incrementing or decrementing a student’s position by 1.

Approach (Greedy + Sorting):
	1.	Sort both arrays: so the closest values are paired together.
	2.	Pair seats[i] with students[i].
	3.	Add the absolute difference between the seat and student positions.
	4.	Return the total sum of those differences.

This greedy pairing ensures the minimal total movement.

⸻

🧠 Example

Input:
Enter the seat positions (space-separated): 3 1 5
Enter the student positions (space-separated): 2 7 4

Output:
✅ Minimum total moves required to seat all students: 4

Explanation:
Sorted seats = [1, 3, 5], Sorted students = [2, 4, 7]
Moves: |1-2| + |3-4| + |5-7| = 1 + 1 + 2 = 4

"""
from typing import List
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        dif = 0
        for i in range(len(seats)):
            dif += abs(seats[i] - students[i])
        return dif


# --------------------------
# 🎯 User Input Handling
# --------------------------
if __name__ == "__main__":
    seats = list(map(int, input("Enter the seat positions (space-separated): ").split()))
    students = list(map(int, input("Enter the student positions (space-separated): ").split()))

    if len(seats) != len(students):
        print("❌ Error: Number of seats and students must be equal.")
    else:
        sol = Solution()
        result = sol.minMovesToSeat(seats, students)
        print("✅ Minimum total moves required to seat all students:", result)