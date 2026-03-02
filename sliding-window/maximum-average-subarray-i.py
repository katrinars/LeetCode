class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        e = k 
        max_avg = float("-inf")

        if len(nums) == k:
            return sum(nums) / k 

        while e < len(nums) + 1: 
            average = sum(nums[s:e]) / k 
            max_avg = max(max_avg, average) 

            s += 1
            e += 1

        return max_avg
