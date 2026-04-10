class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0] 
        max_p = 0
        for x in prices:
            max_p =  max(max_p, x - minBuy)
            minBuy = min(minBuy, x)
        return max_p

