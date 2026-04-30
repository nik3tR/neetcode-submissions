class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mostProfit = 0
        l, r = 0, 1

        while r < len(prices):
            mostProfit = max(mostProfit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return mostProfit

# [10,1,5,6,7,1]
