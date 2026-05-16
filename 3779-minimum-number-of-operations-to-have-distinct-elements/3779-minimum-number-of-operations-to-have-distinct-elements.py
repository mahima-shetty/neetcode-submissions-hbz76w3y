class Solution:
    def minOperations(self, nums: List[int]) -> int:
        seen = set()

        for i in range(len(nums)-1, -1, -1):
            if nums[i] in seen:
                return ceil(i//3) + 1
            
            seen.add(nums[i])
        
        return 0