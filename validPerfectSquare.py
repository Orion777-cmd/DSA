class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 0
        hi = num
        if num == 1: return True
        while lo < hi:
            mid = (lo + hi)//2
            
            if mid**2 == num:
                return True
            elif mid **2 < num:
                lo = mid + 1
            else:
                hi = mid 
        return False
