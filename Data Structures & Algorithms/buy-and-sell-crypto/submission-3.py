class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # maxP = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         if prices[i] < prices[j]:
        #             profit = prices[j] - prices[i]
        #             maxP = max(maxP, profit)
        # return maxP

        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else: 
                l = r
            r += 1
        return maxP

