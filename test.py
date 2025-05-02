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