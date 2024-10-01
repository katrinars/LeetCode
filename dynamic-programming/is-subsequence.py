class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c = 0
        for char in t:
            if s[c] == char:
                c += 1
            if c > len(s) - 1:
                return True
        return False

        