class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        
        rows,cols = len(image),len(image[0])
        
        def dfs(x,y,grid):
           
            if x<0 or x>=rows or y<0 or y>=cols:
                return 
        
            if start_color != grid[x][y] or grid[x][y]==color:
                return
       
            grid[x][y] = color
            
            dfs(x-1,y,grid)
            dfs(x,y-1,grid) 
            dfs(x+1,y,grid) 
            dfs(x,y+1,grid) 
        

        dfs(sr,sc,image)
        return image
