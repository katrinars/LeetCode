class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == nums[mid-1]: # mid = mid-left
                if (mid - left - 1) % 2 == 0: # left-1 is even, search right
                    left = mid + 1
                else: 
                    right = mid - 1
            elif nums[mid] == nums[mid+1]: # mid = mid-right
                if (right - mid - 1) % 2 == 0: # right-1 is even, search left
                    right = mid - 1
                else: 
                    left = mid + 1
            else:
                return nums[mid]
