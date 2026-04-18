class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)

        for n in nums:
            count[n] += 1 

        j = 0
        for i in range(3):
            while count[i] > 0:
                nums[j] = i
                count[i] -= 1
                j += 1
        return nums





        
        