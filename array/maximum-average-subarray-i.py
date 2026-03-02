class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        e = k 
        max_avg = 0 # 51/4

        if len(nums) == k:
            return sum(nums) / k 

        while e < len(nums): # e = 3 --- len(nums) = 6
            average = sum(nums[s:e]) / k 
            max_avg = max(max_avg, average) 
            print(average, max_avg)

            s += 1
            e += 1

        return max_avg
