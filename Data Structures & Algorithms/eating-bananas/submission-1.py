class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_k = r

        while l <= r:
            mid = (l + r) // 2
            total_t = 0
            for p in piles:
                total_t += (p + mid -1) // mid
            if total_t <= h:
                min_k = mid
                r = mid -1
            else:
                l = mid + 1 
        return min_k




