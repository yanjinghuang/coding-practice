class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        double = 0
        missing = 0
        seen = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] in seen:
                    double = grid[r][c]
                seen.add(grid[r][c])

        
        for num in range(1, len(grid) * len(grid) + 1):
            if num not in seen:
                missing = num
            
        return [double, missing]
