class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        vowels = 'aeiouAEIOU'
        s2 = list(s)

        while l < r:
            if s2[l] not in vowels:
                l += 1
            elif s2[r] not in vowels:
                r -= 1
            else:
                s2[l], s2[r] = s2[r], s2[l]
                l += 1
                r -= 1
        
        return ''.join(s2)


