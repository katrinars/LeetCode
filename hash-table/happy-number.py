class Solution:
    def isHappy(self, n: int) -> bool:
        print(n)
        if n == 1: return True
        elif n == 4: return False
        else:
            return self.isHappy((n % 10)**2 + self.getDigits(n // 10))
            
   
    def getDigits(self, n):
        if n < 10:
            return n**2
        else:
            return (n % 10)**2 + self.getDigits(n // 10)

