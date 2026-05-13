class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        x, y = {}, {}
        for i in range(len(s)):
            x[s[i]] = i
        for i in range(len(t)):
            y[t[i]] = i
        ans = 0
        for char in s:
            ans += abs(x[char] - y[char])
        return ans
