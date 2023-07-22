class Solution:
    def romanToInt(self, s: str) -> int:
        dict_ = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C': 100, 
            'D': 500,
            'M': 1000,
        }
        res = 0
        i = len(s)-1
        while i >= 0:
            if i > 0 and dict_[s[i-1]] < dict_[s[i]]:
                res += dict_[s[i]]
                j = i
                i -= 1
                while i >= 0 and dict_[s[i]] < dict_[s[j]]:
                    res -= dict_[s[i]]
                    i -= 1
                
            else:
                res += dict_[s[i]]
                i -= 1
            
        return res
