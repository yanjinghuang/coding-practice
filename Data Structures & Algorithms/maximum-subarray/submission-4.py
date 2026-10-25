class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = float('-inf')

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0 
            cur_sum += n
            max_sum = max(cur_sum, max_sum)
        
        return max_sum
        