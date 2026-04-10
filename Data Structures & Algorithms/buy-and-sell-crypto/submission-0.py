class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rightMax = 0
        array = []
        for i in range(len(prices) -1, -1, -1):
            rightMax = max(prices[i], rightMax)
            array.append(rightMax)

        array.reverse()
        max_sum = -1
        for i in range(len(array)):
            max_sum = max(max_sum, abs(array[i]-prices[i]))
        return max_sum

