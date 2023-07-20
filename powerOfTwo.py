import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        val = math.floor(math.log(n, 2))
        if 2**val == n:
            return True
        else: 
            return False
