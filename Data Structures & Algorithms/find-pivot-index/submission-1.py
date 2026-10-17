class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # prefix sum -> runing left sum, compute right sum using total 
        total = sum(nums)
        leftSum = 0


        for i in range(len(nums)):
            rightSum  = total - nums[i] - leftSum  
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        
        return -1 

            
