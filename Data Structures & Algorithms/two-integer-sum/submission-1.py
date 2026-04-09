class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 3,4,5,6
        # target = 7
        lookup = {}
        for i, x in enumerate(nums) :
            complement = target - x
            if complement in lookup:
                return [lookup[complement], i]
            lookup[x] = i
            # {4:0, 3:1, 2:2, 1:3}
    
