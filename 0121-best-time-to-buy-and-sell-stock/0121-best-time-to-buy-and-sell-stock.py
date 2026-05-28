class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        start = prices[0]
        profit = 0

        for i in range(len(prices)) :
            start = min(start, prices[i])
            profit = max(profit, prices[i] - start)

        return profit
            
        