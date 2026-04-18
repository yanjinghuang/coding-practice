class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        def swap (nums, l , r):
            while l < r:
                nums[l], nums[r] =  nums[r], nums[l]
                l += 1
                r -= 1
            
        l = 0 
        r = len(nums) -1 
        swap(nums, l, r)
        swap(nums, l, k-1)
        swap(nums, k, r)
