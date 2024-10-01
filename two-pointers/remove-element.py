class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)

        while nums:
            try:
                nums.remove(val)
            except ValueError:
                return len(nums)
            