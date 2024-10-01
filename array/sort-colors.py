class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0 == red, 1 == white, 2 == blue
        
        red = nums.count(0)
        white = nums.count(1)
        blue = nums.count(2)

        for i in range(red):
            nums[i] = 0
        for i in range(white):
            nums[red + i] = 1
        for i in range(blue):
            nums[red + white + i] = 2