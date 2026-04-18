class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Counting sort 
        count = defaultdict(int)

        for n in nums:
            count[n] += 1 
        
        # Overwrite the array

        j = 0 
        for i in range(3):
            while count[i] > 0:
                count[i] -= 1
                nums[j] = i
                j +=1
                
        return nums
                




        
        