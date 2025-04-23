class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        curr_length = 0
        stack = []

        matches = {
            '[': ']',
            '(': ')',
            '{': '}'
        }

        for char in s:
            if char in matches:
                stack.append(char)
            else:
                if not stack:
                    max_length = max(max_length, curr_length)
                    curr_length = 0
                    continue
                if matches[stack.pop()] == char:
                    curr_length += 2
                else:
                    max_length = max(max_length, curr_length)
                    curr_length = 0
        max_length = max(max_length, curr_length)
        return max_length
        



        