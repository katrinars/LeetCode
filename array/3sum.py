class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        understand
        - return the index or the value? value
        - can't repeat indices but can repeat numbers
        - can return multiple solutions

        plan
        - intialize an empty list
        - nums.sort() 
        - initialize variable to track len(nums)
        - use index pointer to iterate loop (0 -> n-2), use two more pointers (j, k) to iterate i+1 -> n-1 and j+1 -> n
        - initialize three pointers, one in the first index, one in the second index, and one at the end, it then becomes a binary search O(logn)
        - 


        - return the list

                x    x         x 
        nums = [-4, -1,-1,0,1, 2]
        '''

        # sort ascending to do binary, get nums length, get temp sum variable and empty result list 
        nums.sort() 
        n = len(nums)
        total = 0
        result = []
        
        for i in range(n-2): # loop entire list except last 2
            if i > 0 and nums[i] == nums[i-1]: # skip repeat values to
                continue
            j, k = i+1, n-1 # j = index after i (2nd), k = last index
            while j < k:
                total = nums[i] + nums[j] + nums[k] # get triplet sum
                if total < 0: # if less than 0, seek a higher mid number
                    j += 1
                elif total > 0: # if greater, seek a lower number
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]]) # if equal, add triplet to result and move mid
                    j += 1
                while j < k and nums[j] == nums[j-1]: # Duplicates inside the binary search
                    j += 1
        
        return result