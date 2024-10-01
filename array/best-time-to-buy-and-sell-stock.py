class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i] = price on i day
        # return max profit or 0 if no profit possible
        # aka lowest buy -> highest sell

        profit = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            profit = max(profit, price - lowest)

    
        return profit




