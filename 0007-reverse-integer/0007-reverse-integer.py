class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True

        x = abs(x)
        print(x)
        orig = x
        rev = 0

        while x > 0:
            rev = (rev*10) + (x % 10)
            x = x//10
        
        if rev > 2**31 - 1:
            return 0

        if neg: return -rev
        else: return rev