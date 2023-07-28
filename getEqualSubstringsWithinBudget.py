class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_length = 0
        temp_cost  =0
        i , j = 0, 0
        
        while i < len(t) and j < len(t):
            if s[j] == t[j]:
                j += 1
            else:
                temp_cost += abs(ord(s[j])- ord(t[j]))
                
                if temp_cost > maxCost:
                    
                    max_length = max(max_length, j -i)
                    while i <= j and temp_cost > maxCost:
                        
                        temp_cost -= abs(ord(s[i])-ord(t[i]))
                        i += 1
                    
                    j += 1
                   
                else:
                    j += 1
                
     
        return max(max_length, j-i) if temp_cost <= maxCost else max_length       
