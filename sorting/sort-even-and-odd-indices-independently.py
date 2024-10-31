class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 2:
            return nums

        lp = 0
        rp = 2
        while rp < len(nums):
            # if odd pointers and val @ pointer 2 < val @ pointer 1, swap pointer vals
            if lp % 2 == 1 and nums[lp] < nums[rp]:
                nums[lp], nums[rp] = nums[rp], nums[lp]
            elif nums[lp] > nums[rp]: # if even pointers and val @ l_pointer > val @ r_pointer, swap pointer vals
                nums[lp], nums[rp] = nums[rp], nums[lp]
            lp += 1
            rp += 1

        return nums
