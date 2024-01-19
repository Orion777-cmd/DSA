class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0        
        rows, cols = len(matrix), len(matrix[0])
        memo = [[float('inf')] * cols for _ in range(rows)]
        
        def isBounded(x, y):
            return 0 <= x < rows and 0 <= y < cols
        
        def dp(row, col):
            if row == 0:
                return matrix[row][col]

            if memo[row][col] != float('inf'):
                return memo[row][col]

            memo[row][col] = matrix[row][col] + min(
                dp(row-1, col-1) if isBounded(row-1, col-1) else float('inf'),
                dp(row-1, col),
                dp(row-1, col+1) if isBounded(row-1, col+1) else float('inf')
            )
            
            return memo[row][col]

        min_sum = min(dp(rows-1, col) for col in range(cols))
        
        return min_sum
