class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin = image[sr][sc]
        ROW = len(image)
        COL = len(image[0])
        dirctions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        if origin == color:
            return image
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or image[r][c] != origin:
                return
            image[r][c] = color
            for dr, dc in dirctions:
                dfs(r+dr, c+dc)

        dfs(sr, sc)
        return image
       