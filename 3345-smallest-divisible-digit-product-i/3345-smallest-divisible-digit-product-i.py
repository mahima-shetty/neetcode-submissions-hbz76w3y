class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n+10):
            product = 1
            for digit in str(i):
                product *= int(digit)
            if product % t == 0:
                return i