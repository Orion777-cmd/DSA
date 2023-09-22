class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def backtrack(comb, openCount, closeCount, totparen):
            nonlocal res
            if len(comb) > totparen * 2:
                return 
            if len(comb) == totparen * 2:
                res.append(comb)
                return
            
            if openCount < totparen:
                backtrack(comb + '(', openCount +1, closeCount, totparen)
            if closeCount < openCount:
                backtrack(comb + ')', openCount, closeCount+1, totparen)

        backtrack('', 0, 0, n)
        return res

        
