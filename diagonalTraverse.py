class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat[0]), len(mat)
        res = []
        temp = []
        for i in range(m+n-1):
            temp.clear()

            r, c = 0 if i < m else i -m + 1, i if i < m else m-1

            while r < n and c > -1:
                temp.append(mat[r][c])
                r += 1
                c -= 1
            if i %2 == 0:
                res.extend(temp[::-1])
            else:
                res.extend(temp)
        return res
