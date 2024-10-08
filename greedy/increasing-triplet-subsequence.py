class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if not nums:
            return False
        
        k = 2
        while k < len(nums):
            if nums[k-2] < nums[k-1] and nums[k-1] < nums[k]:
                return True
            k += 1

        return False