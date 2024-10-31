class Solution:
    def addDigits(self, num: int) -> int:
        if num // 10 == 0:
            return num

        sum = num % 10 + self.addDigits(num // 10)

        if sum < 10:
            return sum
        else:
            return self.addDigits(sum)
