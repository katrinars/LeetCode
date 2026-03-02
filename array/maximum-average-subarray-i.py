class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        e = k 
        highest_sum = float("-inf")
        # max_avg = float("-inf")

        if len(nums) == k:
            return sum(nums) / k 

        while e < len(nums) + 1: 
            new_sum = sum(nums[s:e])
            highest_sum = max(highest_sum, new_sum) 

            s += 1
            e += 1

        return highest_sum / k
