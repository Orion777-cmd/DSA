class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        '''
        1 2 3      1 3 6     
        4 5 6      10 15 21
        7 8 9      28 36 45
        
        ''' 
        rows = len(mat)
        col = len(mat[0])
        prefixSum = [[0] * col for _ in range(rows) ]

        prefixSum[0][0] = mat[0][0]
        for j in range(1, col):
            prefixSum[0][j] = mat[0][j] + prefixSum[0][j-1]

       
        for i in range(1, rows):
            prefixSum[i][0] = mat[i][0] + prefixSum[i-1][0]

     
        for i in range(1, rows):
            for j in range(1, col):
                prefixSum[i][j] = mat[i][j] + prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1]
        print(prefixSum)
        ans = [[0] * col for _ in range(rows)]

        for i in range(rows):
            for j in range(col):
                r1, r2 = max(0, i - k), min(rows - 1, i + k)
                c1, c2 = max(0, j - k), min(col - 1, j + k)
                
                ans[i][j] = prefixSum[r2][c2]
                
                if r1 > 0:
                    ans[i][j] -= prefixSum[r1 - 1][c2]
                
                if c1 > 0:
                    ans[i][j] -= prefixSum[r2][c1 - 1]
                
                if r1 > 0 and c1  > 0:
                    ans[i][j] += prefixSum[r1 - 1][c1 - 1]
        
        return ans
      
