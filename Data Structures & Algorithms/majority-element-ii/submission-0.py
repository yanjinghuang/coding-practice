from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = Counter(nums)
        res = []

        for c, f in count.items():
            if f > n // 3:
                res.append(c)

        return res 
        
        