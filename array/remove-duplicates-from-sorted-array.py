class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 1

        while p2 < len(nums):
            if nums[p1] != nums[p2]:
                p1 += 1
                p2 += 1
            else:
                nums.remove(nums[p2])

            
        