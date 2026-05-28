class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        v = sorted(v)
        v1 = v[0]
        v2 = v[-1]
        res = ""


        for i in range(min( len(v1), len(v2) )):
            if v1[i] != v2[i] :
                break
            res = res + v1[i]

        return res