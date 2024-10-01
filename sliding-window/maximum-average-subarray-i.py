class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = 0
        p = k-1

        if len(nums) == k:
            return sum(nums) / k

        while p <= len(nums) - 1:
            curr_avg = sum(nums[p+1-k:p+1]) / k
            if curr_avg > max_avg:
                max_avg = curr_avg
            p += 1
        return max_avg