class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l, r = 0, 1 # [10,1,5,6,7,1]
        # maxP = 0

        # while r < len(prices): # while r is less than list size
        #     if prices[l] < prices[r]: # if buy price, less than sell price
        #         profit = prices[r] - prices[l] #profit for that day = sell - buy
        #         maxP = max(profit, maxP) # compare this profit to largest maxP seen
        #     else:
        #         l = r # if buy > sell, make that sell the new buy price. buying lower is always better.
        #     r += 1
        # return maxP

        maxP = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[i] < prices[j]:
                    profit = prices[j] - prices[i]
                    maxP = max(maxP, profit)
        return maxP