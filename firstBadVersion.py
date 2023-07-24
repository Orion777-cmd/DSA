# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo =0
        hi = n
        while lo < hi:
            mid = (lo+hi)//2

            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid) and isBadVersion(mid-1):

                hi = mid
            else:
                lo = mid + 1
        return n
