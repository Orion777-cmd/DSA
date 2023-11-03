class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 1, n
        if n == 1: return 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if (mid * (mid+1)) // 2 == n:
                return mid
            elif ((mid * (mid+1)) // 2) > n:
                hi= mid-1
            else:
                lo= mid+1
        return hi
