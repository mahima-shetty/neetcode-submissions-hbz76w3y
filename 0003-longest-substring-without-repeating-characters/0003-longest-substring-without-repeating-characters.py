class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        charSet = set()
        count = 0
        right = 0
        for right in range( len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1

            charSet.add(s[right])
            count = max(count, right - left + 1)
        
        
        print(charSet)    
        return (count)