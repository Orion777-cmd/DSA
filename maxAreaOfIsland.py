class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        area = 0
        def dfs(grid, x, y):
            nonlocal area
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
                return 
            
            area += 1
            grid[x][y] = 0
            dfs(grid, x+1, y)
            dfs(grid, x-1, y)
            dfs(grid, x, y-1)
            dfs(grid, x, y+1)

            return 
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    dfs(grid, x, y)
                    res = max(area, res)
                    area = 0
        return res
