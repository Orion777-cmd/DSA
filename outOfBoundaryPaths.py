class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        modulo = 10 ** 9 + 7 
        memo = {}
        
        def outOfBound(x: int , y: int) -> bool:
            return x < 0 or x >= m or y < 0 or y >= n
        
        def dp(i: int, j: int, moveLeft: int, ways: int) -> int:
            if moveLeft < 0:
                return 0
            if outOfBound(i, j):
                return 1
            
            if (i, j, moveLeft) in memo:
                return memo[(i, j, moveLeft)]
            
            ways = (ways + dp(i + 1, j, moveLeft - 1, 0)) % modulo
            ways = (ways + dp(i - 1, j, moveLeft - 1, 0)) % modulo
            ways = (ways + dp(i, j + 1, moveLeft - 1, 0)) % modulo
            ways = (ways + dp(i, j - 1, moveLeft - 1, 0)) % modulo
            
            memo[(i, j, moveLeft)] = ways
            return ways
        
        return dp(startRow, startColumn, maxMove, 0)
