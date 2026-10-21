from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bounded (freq 1 : n-1) - > bucket sort
        # idx = freq -> big idx first
        # count, flip, collect 

        freq = Counter(nums)
        n = len(nums)
        bucket = [[] for i in range (n + 1)]
        res = []

        for num, count in freq.items():
            bucket[count].append(num)

        
        for i in range(n , 0, -1):
            for items in bucket[i]:
                res.append(items)
                if len(res) == k:
                    return res
        
        return res 


        
        
        
        