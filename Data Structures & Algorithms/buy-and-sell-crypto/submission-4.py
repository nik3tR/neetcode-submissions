class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while l < r and r < len(prices):
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxP


