class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        length = len(grid)
        direction = [[0,1], [1,0], [-1,0], [0, -1]]

        def invalid(r, c):
            return r < 0 or c < 0 or r == length or c == length
        
        visited = set()

        def dfs(r, c):
            if(invalid(r, c) or not grid[r][c] or (r,c) in visited):
                return 
            visited.add((r,c))
            for dr, dc in direction:
                dfs(dr+r, dc+c)
        
        def bfs():
            res , queue = 0, deque(visited)
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in direction:
                        newR, newC = r +dr, c + dc
                        if invalid(newR, newC) or (newR, newC) in visited:
                            continue
                        if grid[newR][newC]:
                            return res
                        queue.append((newR, newC))
                        visited.add((newR, newC))
                res += 1
        for i in range(length):
            for j in range(length):
                if grid[i][j]:
                    dfs(i, j)
                    return bfs()
