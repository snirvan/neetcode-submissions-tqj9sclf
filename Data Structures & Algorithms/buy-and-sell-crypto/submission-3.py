class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left pointer
        # incrament right pointer via loop
        # if prices[right] - prices[left]:
        # calculate profit and 
        maxProfit = 0 
        l = 0

        for r in range(1,len(prices)):
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r]- prices[l])
            else:
                l = r

        return maxProfit

            



    