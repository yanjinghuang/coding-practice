class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        to_set = set(nums)
        if len(nums) > len(to_set):
            return True
        else:
            return False
        