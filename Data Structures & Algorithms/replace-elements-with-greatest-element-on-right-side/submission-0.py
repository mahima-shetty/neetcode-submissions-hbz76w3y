class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        new_arr = [0]*len(arr)

        for i in range(len(arr)):
            rightmax = -1
            for j in range(i+1, len(arr)):
                rightmax = max(arr[j], rightmax)
            new_arr[i] = rightmax


        return new_arr 

        