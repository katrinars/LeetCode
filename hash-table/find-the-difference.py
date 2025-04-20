class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letter = set(t) - set(s)
        return letter.pop()