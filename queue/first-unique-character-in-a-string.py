class Solution:
    def firstUniqChar(self, s: str) -> int:
        for char in s:
            first = s.find(char)
            last = s.rfind(char)
            if last == first:
                return first
            else: continue
        return -1
