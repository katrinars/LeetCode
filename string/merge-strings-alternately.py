class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p = 0
        alt_chars = []
        

        while p <= len(word1) - 1 and p <= len(word2) - 1:
            alt_chars.append(word1[p])
            alt_chars.append(word2[p])
            p += 1
        if len(word1) > p:
            alt_chars.append(word1[p:])
        if len(word2) > p:
            alt_chars.append(word2[p:])
        # print(alt_chars)

        return ''.join(alt_chars)
