class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []

    
        def backtrack(combination, digits):
            if not digits:
                res.append(combination)
                return
            for i in phone[digits[0]]:
                backtrack(combination + i, digits[1:])
        
        backtrack("", digits)
        return res
