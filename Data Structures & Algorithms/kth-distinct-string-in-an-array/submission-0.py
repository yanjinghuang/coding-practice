class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        res = []

        for ch, cnt in count.items():
            if cnt == 1:
                res.append(ch)
            if cnt == 1 and len(res) == k: return ch
            
        return ""
        