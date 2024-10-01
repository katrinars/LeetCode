class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        diff = {}
        res = 0

        for num in nums:
            if num in diff:
                if diff[num] % 2 == 1:
                    res += 1
            rem = k - num
            diff[rem] = diff.get(rem, 0) + 1

        return res