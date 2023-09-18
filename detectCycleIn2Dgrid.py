class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(x, y, parent_x, parent_y):
            if (x, y) in visited:
                return True

            visited.add((x, y))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (
                    0 <= new_x < rows
                    and 0 <= new_y < cols
                    and grid[new_x][new_y] == grid[x][y]
                    and (new_x, new_y) != (parent_x, parent_y)
                ):
                    if dfs(new_x, new_y, x, y):
                        return True

            return False

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited:
                    if dfs(i, j, -1, -1):
                        return True

        return False
