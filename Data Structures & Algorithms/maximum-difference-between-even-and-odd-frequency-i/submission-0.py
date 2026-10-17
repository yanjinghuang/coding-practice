class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)

        oddMax = 0
        evenMin = float('inf')

        for cnt in count.values():
            if cnt & 1:
                oddMax = max(oddMax, cnt)
            else:
                evenMin = min(evenMin, cnt)
        
        return oddMax - evenMin


        