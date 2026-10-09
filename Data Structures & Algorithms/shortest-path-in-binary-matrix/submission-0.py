from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1

        visited = {(0,0)}
        queue = deque([(0,0,1)])
        directions = [(0,1), (1,0), (0,-1),(-1, 0),
                     (1,1), (-1,-1), (-1,1), (1,-1)]
        n = len(grid)

        
        while queue:
            r, c, d = queue.popleft()
            if r == n-1 and c == n-1: return d 

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr, nc, d+1))
        return -1

            
        





