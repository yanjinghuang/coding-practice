class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # min() set a inf big 

        l = 0 
        total = 0 
        res = float('inf')

        for r in range(len(nums)):
            total += nums[r]
            # when meet the requirement 
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        
        return 0 if res == float('inf') else res

