class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s:
            return False
        
        res = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                res.append(i)
            
            else:
                if not res:
                    return False

                a = res.pop()
                if i == ')' and a != '(':
                    return False
                if i == '}' and a != '{':
                    return False
                if i == ']' and a != '[':
                    return False
        return len(res) == 0