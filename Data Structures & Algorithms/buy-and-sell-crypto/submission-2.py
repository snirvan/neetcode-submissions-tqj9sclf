class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0

        for right in range(1,len(prices)):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                if profit > 0:
                    maxProfit = max(profit, maxProfit)
            else:
                left = right
        
        return maxProfit

        