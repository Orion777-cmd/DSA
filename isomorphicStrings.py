class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            dict = {}
        
            for i in range(len(s)):
                c1 = s[i]
                c2 = t[i]
                if c1 in dict.keys() and dict.get(c1) != c2:
                    return False
                elif c2 in dict.values() and c1 not in dict.keys():
                    return False
                else:
                    dict.update({c1:c2})
        
        return True 
