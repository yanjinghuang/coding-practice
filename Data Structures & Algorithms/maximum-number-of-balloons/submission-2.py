class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hmap = defaultdict(int) 

        for c in text:
            if c in 'balon':
                hmap[c] += 1 

        
        return min(hmap['b'], hmap['a'],hmap['l']//2, hmap['o']//2,
        hmap['n'])
