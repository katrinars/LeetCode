class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for char in magazine:
            letters[char] = letters.get(char, 0) + 1
        print(letters)
        for char2 in ransomNote:
            try:
                if letters[char2] > 0:
                    letters[char2] -= 1
                else:
                    return False
            except:
                return False
        return True
            