class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = blocks[:k].count('W')
        best = w

        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                w -= 1
            if blocks[i] == "W":
                w += 1
            best = min(best, w)
        
        return best



        