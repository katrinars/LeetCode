class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        match = {}
        i = 0
        s = s.split()

        if len(pattern) != len(s):
            return False

        while i < len(pattern):
            if pattern[i] in match:
                if match[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] not in match.values():
                    match[pattern[i]] = s[i]
                else:
                    return False
            i += 1
        
        return True