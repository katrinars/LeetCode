class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replace = {}
        if s == t:
            return True
        for i, char in enumerate(s):
            if char not in replace.keys():
                if t[i] not in replace.values():
                    replace[char] = t[i]  
                else:
                    return False
            else:
                if replace[char] == t[i]:
                    continue
                else:
                    return False
        return True
        
        