class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     j = i + 1
        #     while j+1 <= len(numbers):
        #         if numbers[i] + numbers[j] == target:
        #             return[i+1, j+1]
        #         else:
        #             j+=1

        l = 0
        r = len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return[l+1, r+1]
            elif sum > target:
                r-=1
            else:
                l += 1