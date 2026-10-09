class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def can_ship(capacity):
            d = 1
            load = 0
            for w in weights:
                if load + w > capacity:
                    d += 1
                    load = 0
                load += w
            return d <= days


        l = max(weights) 
        r = sum(weights)
        min_w  = r 

        while l <= r:
            mid = (l + r) // 2
            if can_ship(mid):
                min_w = mid
                r = mid - 1 
            else:
                l = mid + 1
        return min_w


        