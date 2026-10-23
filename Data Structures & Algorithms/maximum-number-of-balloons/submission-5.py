class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hmap = defaultdict(int)


        for c in text:
            if c in 'balon':
                hmap[c] += 1

        if len(hmap) < 5:
            return 0 
        
        hmap['l'] //= 2
        hmap['o'] //= 2

        return min( hmap.values())

        