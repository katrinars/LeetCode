class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        p1 = 0
        count = 0

        while p1 < len(nums):
            for p2 in range(p1 + 1, len(nums)):
                if nums[p1] + nums[p2] < target:
                    count += 1
            p1 += 1

        return count

        