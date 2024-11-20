class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # frequency dictionary -- not constant space
        # .find and .rfind -- not linear time
        # sort and check i and i+1 -- linear and no extra space


        nums.sort() # O(n)
        p1 = 0
        p2 = 1

        while p2 < len(nums):  # O(n)
            if nums[p1] == nums[p2]:
                p1 += 2
                p2 += 2
            else:
                return nums[p1]
        return nums[p1] # O(1)

