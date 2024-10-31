class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        lp = 0
        rp = 1

        while rp < len(nums):
            if nums[lp] == nums[rp]:
                lp += 2
                rp += 2
            else:
                return nums[lp]
        if rp > len(nums) - 1:
            return nums[lp]

        return nums[rp]
        


