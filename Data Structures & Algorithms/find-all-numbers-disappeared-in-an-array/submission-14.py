class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # flag missing index by negating -> missing num = postive index value 

        for n in nums:
            i = abs(n) - 1 
            nums[i] = -abs(nums[i]) 
        
        return [i + 1 for i, n in enumerate(nums) if n > 0]
        