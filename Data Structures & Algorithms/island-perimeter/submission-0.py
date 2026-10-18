class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # each cell contribute 4 perimeter but if it has 
        # neigbord land they share the edge
        total = 0
        ROW = len(grid)
        COL = len(grid[0])

        for r in range(ROW):
            count = 0
            for c in range(COL):
                if grid[r][c] == 1:
                    count += 4
                    # if not first row , col look back and discounted
                    if r and grid[r-1][c] == 1:
                        count -= 2
                    if c and grid[r][c-1] == 1:
                        count -= 2 
            total += count
        return  total 
                    