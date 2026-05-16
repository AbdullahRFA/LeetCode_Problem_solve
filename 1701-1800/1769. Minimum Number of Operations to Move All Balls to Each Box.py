
'''
1769. Minimum Number of Operations to Move All Balls to Each Box
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.
In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.
Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.
Example 1:
Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for the first box is as follows:
- Move the ball from the second box to the first box in 1 operation.
The answer for the second box is as follows:
- Move the ball from the first box to the second box in 1 operation.
The answer for the third box is as follows:
- Move the ball from the first box to the third box in 2 operations.
- Move the ball from the second box to the third box in 1 operation.
The total number of operations for the third box is 3.
Example 2:
Input: boxes = "001011"
Output: [11,8,5,4,3,4]
Explanation: The answer for the first box is as follows:
- Move the ball from the fourth box to the first box in 3 operations.
- Move the ball from the fifth box to the first box in 2 operations.
- Move the ball from the sixth box to the first box in 1 operation.
The total number of operations for the first box is 3 + 2 + 1 = 6.
- Move the ball from the fourth box to the second box in 2 operations.
- Move the ball from the fifth box to the second box in 1 operation.
- Move the ball from the sixth box to the second box in 2 operations.
The total number of operations for the second box is 2 + 1 + 2 = 5.
- Move the ball from the fourth box to the third box in 1 operation.
- Move the ball from the fifth box to the third box in 2 operations.
- Move the ball from the sixth box to the third box in 3 operations.
The total number of operations for the third box is 1 + 2 + 3 = 6.
- Move the ball from the fourth box to the fourth box in 0 operations.
- Move the ball from the fifth box to the fourth box in 1 operation.
- Move the ball from the sixth box to the fourth box in 2 operations.
The total number of operations for the fourth box is 0 + 1 + 2 = 3.
- Move the ball from the fourth box to the fifth box in 1 operation.
- Move the ball from the fifth box to the fifth box in 0 operations.
- Move the ball from the sixth box to the fifth box in 1 operation.
The total number of operations for the fifth box is 1 + 0 + 1 = 2.
- Move the ball from the fourth box to the sixth box in 2 operations.
- Move the ball from the fifth box to the sixth box in 1 operation.
- Move the ball from the sixth box to the sixth box in 0 operations.
The total number of operations for the sixth box is 2 + 1 + 0 = 3.
Constraints:    
n == boxes.length
1 <= n <= 2000
boxes[i] is either '0' or '1'.

Intuition:
To solve the problem, we can use a two-pass approach to calculate the minimum number of operations needed to move all the balls to each box.
1. In the first pass, we can iterate through the boxes from left to right and calculate the number of operations needed to move all the balls to the current box from the left side. We can keep track of the number of balls and the total operations needed as we iterate through the boxes.
2. In the second pass, we can iterate through the boxes from right to left and calculate the number of operations needed to move all the balls to the current box from the right side. We can again keep track of the number of balls and the total operations needed as we iterate through the boxes.

Approach:
1. Initialize an array `answer` of size n with all elements set to 0.
2. Initialize two variables `opts` and `balls` to 0. `opts` will keep track of the total operations needed, and `balls` will keep track of the number of balls encountered so far.
3. Iterate through the boxes from left to right:
   - For each box, add the current value of `opts` to `answer[i]`.
   - If the current box contains a ball (i.e., `boxes[i] == '1'`), increment the `balls` count.
   - Update `opts` by adding the current `balls` count to it, since each ball will require one additional operation to move to the next box.
4. Reset `balls` and `opts` to 0 for the second pass.
5. Iterate through the boxes from right to left:
   - For each box, add the current value of `opts` to `answer[i]`.
   - If the current box contains a ball, increment the `balls` count.
   - Update `opts` by adding the current `balls` count to it, since each ball will require one additional operation to move to the previous box.
6. Return the `answer` array as the final result.

Time Complexity: O(n), where n is the length of the input string `boxes`, since we need to iterate through the boxes twice.
Space Complexity: O(n), since we are using an additional array `answer` of size n to store the results.



'''

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0]*n

        opts = 0
        balls = 0

        for i in range(n):
            answer[i]+=opts
            if boxes[i]=="1":
                balls+=1

            opts+=balls
        
        balls=0
        opts=0

        for i in range(n-1,-1,-1):
            answer[i]+=opts
            if boxes[i]=="1":
                balls+=1

            opts+=balls

            
        return answer


