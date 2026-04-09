class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        new_arr = [0]*len(arr)
        n = len(arr)
        rightMax = -1
        for i in range(n-1,-1,-1):
            new_arr[i] = rightMax
            rightMax = max(rightMax, arr[i])

            


        return new_arr 

        