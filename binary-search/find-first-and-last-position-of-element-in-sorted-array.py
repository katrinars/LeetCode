class Solution:
    def find_range(nums, target, found):
        l = found
        r = found
        print(l, r)
        while l > 0 and r < len(nums):
            if nums[l-1] != target and nums[r+1] != target:
                return [l, r]
            elif nums[l-1] == target:
                print('test', nums[l-1], l)
                l = l-1
            elif nums[r+1] == target:
                r = r + 1
        return [l, r]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        if not nums: 
            return [-1, -1]

        while l <= r:
            m = (l + r) // 2
            print(l, m, r)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            elif nums[m] == target:
                print(2)
                return Solution.find_range(nums, target, m)
        return [-1, -1]

    

