class Solution:
    def lengthOfLongestSubstring(self, string1: str) -> int:
        # abcabcbb
        charSet = set()
        l = 0
        res = 0
        for r in range(len(string1)):
            while string1[r] in charSet:
                charSet.remove(string1[l])
                l += 1
            charSet.add(string1[r])
            res = max(res, r - l +1)
        return res




