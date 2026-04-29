class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr_sub = [ [i, nums[i]] for i in range(len(nums)) ]

        arr_sub.sort(key = lambda x : x[1], reverse = True)
        print(arr_sub)
        vals = sorted(arr_sub[:k])
        res = [val for idx, val in vals]
        return res
