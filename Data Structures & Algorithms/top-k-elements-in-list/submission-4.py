class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int) # {n: count}

        for n in nums:
            res[n] += 1
        sorted_keys = sorted(res.keys(), key=lambda x: res[x], reverse=True)
        return list(sorted_keys[:k])