class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 3 or n==1:
            return True
        elif n < 3:
            return False
        return self.isPowerOfThree(n/3)
        