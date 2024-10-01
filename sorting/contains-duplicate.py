class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniq_nums = set(nums)
        if len(uniq_nums) == len(nums):
            return False
        else:
            return True
        