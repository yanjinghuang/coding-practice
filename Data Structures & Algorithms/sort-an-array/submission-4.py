class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # count frequency, find min and max value, set index then decrement in count

        count = defaultdict(int)
        smallest = min(nums)
        largest = max(nums)

        for n in nums:
            count[n] += 1
        
        i = 0 
        for n in range(smallest, largest+1):
            while count[n] > 0:
                nums[i] = n
                i += 1 
                count[n] -=1 
        
        return nums
        




        