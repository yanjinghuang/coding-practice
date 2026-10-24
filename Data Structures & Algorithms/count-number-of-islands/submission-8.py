class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        ROW = len(grid)
        COL = len(grid[0])
        count = 0

        def dfs(r, c):
            if r >= ROW or r < 0 or c < 0 or c >= COL or grid[r][c]== "0":
                return 
            
            grid[r][c] = "0"
            
            for dr, dc in direction:
                dfs(r + dr, c + dc)
        

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    count += 1 
                    dfs(r,c)
                    
        
        return count 


        
        