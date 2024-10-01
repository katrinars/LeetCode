class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        greatest = max(candies) # current greatest candy val
       
        # iterate through candies, add extras, test against greatest, append to result
        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= greatest)
        
        return result





