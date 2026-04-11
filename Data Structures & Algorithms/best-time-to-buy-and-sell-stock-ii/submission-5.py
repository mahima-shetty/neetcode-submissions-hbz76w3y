class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = -1
        answer = 0
        for i in range(len(prices)-1):
            j = i + 1
            if prices[i] < prices[j]:
                max_p =  prices[j] - prices[i]
                answer += max_p
                print(max_p)

        return answer    
