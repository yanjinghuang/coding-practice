class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        res = []
        
        # [cnt : [n1, n2]]
        bucket = [[] for i in range(len(nums) + 1)]
        for n, cnt in count.items():
            bucket[cnt].append(n)

        for i in range(len(nums), 0, -1):
            for item in bucket[i]:
                res.append(item)
                if len(res) == k:
                    return res

        return res

            


