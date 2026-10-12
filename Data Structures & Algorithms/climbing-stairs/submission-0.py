import math
class Solution:
    def climbStairs(self, n: int) -> int:
        # ... n -1 or n - 2 only last two values matter
        # bottom up DP - from base to work all the way up 

        one, two = 1, 1 # way(n-1), way(n)
        for _ in range(n-1):
            temp = one + two
            one, two  = two, temp
        
        return two