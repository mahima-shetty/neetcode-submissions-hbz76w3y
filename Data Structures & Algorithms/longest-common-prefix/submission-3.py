class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = strs[0] #flo flow, flower, flog
        # you will get the prefix as first element
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(strs[i]) , len(prefix) ):
        # start from flow  1,len(strs)  
        # loop
            # index j initialize - flow + prefix - if found disruption
                if prefix[j] != strs[i][j]:
                    break
                j+=1
            prefix = prefix[:j]
            
            # update prefix 
        return prefix

        


        

