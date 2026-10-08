class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) -1 

        while l < r:
            m = (l + r) // 2
            if m & 1:
                m -= 1
            if nums[m] != nums[m+1]:
                r = m
            else:
                l += 2
        return nums[l]




