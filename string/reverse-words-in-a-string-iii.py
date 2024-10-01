class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        chars = []
        
        for i, word in enumerate(words):
            p = len(word) - 1
            while p >= 0:
                chars.append(word[p])
                p -= 1
            if i < len(words) - 1:
                chars.append(' ')
        return ''.join(char for char in chars)
        