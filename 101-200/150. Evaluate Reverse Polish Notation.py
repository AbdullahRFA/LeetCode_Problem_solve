from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for char in tokens:
            if char in "+-*/":
            
                num2 = stack.pop()
                num1 = stack.pop()

                if char == '+':
                    temp = num1 + num2
                    stack.append(temp)
                elif char == '-':
                    temp = num1 - num2
                    stack.append(temp)
                elif char == '*':
                    temp = num1 * num2
                    stack.append(temp)
                elif char == '/':
                    temp = int(num1 / num2)
                    stack.append(temp)
            else:
                stack.append(int(char))
        return stack[-1]

