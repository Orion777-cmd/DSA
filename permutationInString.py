class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        i, j = 0 , 0
        str1 = list(s1)
        str2 = list(s2)
        str1.sort()
        n = len(s2)
        length = len(s1)
        while i < n-1 and j < n-1:
            while j -i +1 != length:
                j += 1
            temp = str2[i:j+1]
            temp.sort()
            if temp == str1:
                return True
            
            i += 1
        return False
        
        
