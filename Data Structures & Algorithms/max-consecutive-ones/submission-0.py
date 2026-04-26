class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_r = -1
        res = 0

        for i in nums:
            if i == 0:
                max_r = max(res, max_r)
                res = 0
            else:
                res += 1
        
        max_r = max(res, max_r)
        return max_r