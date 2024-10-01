class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            p1 = 0
            p2 = len(word) - 1
            while p1 <= p2:
                if word[p1] == word[p2]:
                    if p1 == p2 or p1+1 == p2:
                        return word
                    p1 += 1
                    p2 -= 1
                else:
                    break
        return ''
        