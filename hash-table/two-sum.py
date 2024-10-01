class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []

        for i, num in enumerate(nums):
            diff = target - num
            try:
                indices.append(nums.index(diff, i+1))
                indices.append(i)
                break
            except:
                continue

        return indices