class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, no in enumerate(nums):
            # 3:0,4:1,5:2,1:3
            complement = target - no #4
            if complement in lookup:
                return [lookup[complement], i]
            lookup[no] = i
