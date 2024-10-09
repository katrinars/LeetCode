class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # check for valid parens
        # for invalid parens, count occurances as number of moves
        if not s:
            return 0
        # create stack, for chars in s
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
        # if char is (, add to stack
            elif char == "(":
                stack.append(char)
        # if TOS is ( and char is ), remove TOS
            elif stack[-1] == "(" and char == ")":
                stack.pop(-1)
        # if char is ) and not last condition, add as TOS
            elif char == ")":
                stack.append(char)

        print(s, stack)

        return len(stack)
            
        