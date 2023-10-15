class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i , j = 0, 0
        
        dict_ = defaultdict(int)
        j = 0
        res = []
        for i in range(10, len(s)+1):
            dict_[s[j:i]] += 1
            j += 1
       
        for key, val in dict_.items():
            if val >1:
                res.append(key)
        return res
