class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.insert(0, char)
            elif char == ')' and stack:
                if stack[0] == '(':
                    stack.pop(0)
                else:
                    return False
            elif char == '}' and stack:
                if stack[0] == '{':
                    stack.pop(0)
                else:
                    return False
            elif char == ']' and stack:
                if stack[0] == '[':
                    stack.pop(0)
                else:
                    return False
            else:
                return False
        return len(stack) == 0