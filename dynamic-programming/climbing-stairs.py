class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        S = [0] * n
        S[0] = 1
        S[1] = 2

        for i in range(2, n):
            S[i] = S[i-1] + S[i-2]

        return S[-1]

        