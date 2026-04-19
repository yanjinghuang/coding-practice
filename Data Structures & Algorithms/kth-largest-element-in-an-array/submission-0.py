class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.k = k 
        heapq.heapify(self.nums)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]

        