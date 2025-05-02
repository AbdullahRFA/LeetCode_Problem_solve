"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true



Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""
"""
🧠 Solution Technique:
	1.	Create a dictionary to match each closing bracket to its corresponding opening bracket.
	2.	Iterate over each character in the string:
	•	If it’s an opening bracket, push it onto the stack.
	•	If it’s a closing bracket, check:
	•	Is the stack empty? If yes → invalid.
	•	Is the top of the stack the correct matching bracket? If yes → pop. If no → invalid.
	3.	After processing, check if the stack is empty. If yes, return True, otherwise False.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        dic_open = {
            ')':'(',
            '}':'{',
            ']':'[',
        }

        list_stack = []
        for x in s:
            if x in dic_open.values():
                list_stack.append(x)
            else:
                if len(list_stack) == 0:
                    return False
                else:
                    if dic_open[x] != list_stack[-1]:
                        return False
                    else:
                        list_stack.pop()

        return len(list_stack) == 0


sl = Solution()
print(sl.isValid("()[]{}"))