# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n ==1: return n
        
        i = 1
        while i < n:
            g = i + n % 2
            print(i, g, n)
            print(guess(g))
            if guess(g) == -1:
                n = g - 1
            elif guess(g) == 1:
                i = g + 1
            else:
                return g