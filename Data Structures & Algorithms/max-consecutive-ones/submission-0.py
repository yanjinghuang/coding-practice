class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_strike = 0
        cur = 0

        for n in nums:
            if n == 1:
                cur += 1
                max_strike = max(cur, max_strike)
            else:
                cur = 0 
        return max_strike