class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        def dfs(board, x,   y):
            if board[x][y] != "E":
                return 
            count = 0
            for r, c in directions:
                nx, ny = r + x, c + y
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[nx][ny] == "M":
                        count += 1
            if count > 0:
                board[x][y] = str(count)
                return 
            board[x][y] = 'B'

            for r, c in directions:
                nx, ny = r + x, c + y
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    dfs(board, nx, ny)


        directions = [(1,1), (1,0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1)]
        i, j = click
        if board[i][j] == "M":
            board[i][j] = "X"
            return board
        else:
            dfs(board, i, j)
            return board
