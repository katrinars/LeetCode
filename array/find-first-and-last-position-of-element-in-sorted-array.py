class Solution:
    def find_range(nums, target, found):
        l = found
        r = found
        while l >= 0 and r < len(nums):
            if nums[l-1] != target and nums[r+1] != target:
                return [l, r]
            elif nums[l-1] == target:
                l = l-1
            elif nums[r+1] == target:
                r = r + 1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        if not nums: return [-1, -1]

        while l < r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            elif nums[m] == target:
                return Solution.find_range(nums, target, m)
        return [-1, -1]

    

