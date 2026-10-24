class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) #idx, cnt
        bucket = [[] for n in range(len(nums) +1 )]
        res = []

        for n, cnt in count.items():
            bucket[cnt].append(n)


        for i in range(len(nums), 0, -1):
            for items in bucket[i]:
                res.append(items)
                if len(res) == k:
                    return res

        return res                

        