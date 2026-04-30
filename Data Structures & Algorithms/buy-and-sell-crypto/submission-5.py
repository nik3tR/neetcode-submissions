class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyIndex = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, prices[i] - prices[buyIndex])
            if prices[i] < prices[buyIndex]:
                buyIndex = i
        return maxProfit
