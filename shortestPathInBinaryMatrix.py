class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if not grid: return -1
        if grid == [[0]]:return 1
        row = len(grid)
        column = len(grid[0])
        queue = [(0, 0, 1)] if grid[0][0]== 0 else []
        grid[0][0] = 1

        while queue:
            # print(queue)
            x, y, length = queue.pop(0)

            for newX in [x-1, x, x+1]:
                for newY in [y-1, y, y+1]:

                    if (x, y) == (row-1, column-1):
                        return length 

                    if 0 <= newX < row and 0 <= newY < column:
                        if grid[newX][newY] == 0:
                            queue.append((newX, newY, length+1))

                            grid[newX][newY] = 1
        return -1

