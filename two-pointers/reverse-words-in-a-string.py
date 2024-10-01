class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        reversed = []
        for word in words[::-1]:
            reversed.append(word)

        return ' '.join(reversed)

        