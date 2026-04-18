class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # duplicates are adjacent to each other, if left does not == current value 
        # need to do it in-place

        if not nums:
            return 0
    
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        # l will be the num of unique values
        return l




                


        