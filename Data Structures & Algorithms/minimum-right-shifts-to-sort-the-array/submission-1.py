class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        nums1 = sorted(nums)
        if nums == nums1:
            return 0
        for i in range(1, len(nums)):
            if nums[i:] + nums[:i] == nums1:
                return len(nums) - i
        return -1 
