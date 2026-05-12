# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [2,7,11,15] 
target = 9



def answer1 (nums: list, target: int) -> list:
    mapp = {}
    for i in range(len(nums)):
        if (target - nums[i] ) in mapp:
            return [ mapp[target - nums[i]], i]
        mapp[nums[i]] = i
    return -1
    
print(answer1(nums, target))
    
    
