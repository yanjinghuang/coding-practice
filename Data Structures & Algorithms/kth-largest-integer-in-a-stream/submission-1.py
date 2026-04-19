class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.mheap = nums
        self.k = k 
        heapq.heapify(self.mheap)

        while len(self.mheap) > self.k:
            heapq.heappop(self.mheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.mheap, val)

        while len(self.mheap) > self.k:
            heapq.heappop(self.mheap)
    
        return min(self.mheap)



        

        
