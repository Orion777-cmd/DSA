class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for brac in s:
            if not stack or brac == '(':
                stack.append(brac)
            elif stack and stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                temp = 0
                while stack and str(stack[-1]).isdigit():
                    temp += stack.pop()
                stack.pop()
                stack.append(2*temp)
        return sum(stack)
