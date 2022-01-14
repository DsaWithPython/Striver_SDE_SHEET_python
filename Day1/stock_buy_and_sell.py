import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0
        min_price = sys.maxsize
        for i in range(0,len(prices)):
            min_price = min(min_price,prices[i])
            profit_max = max(profit_max,prices[i]-min_price)
            
        return profit_max
        
