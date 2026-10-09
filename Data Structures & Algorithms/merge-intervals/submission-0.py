class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged = [intervals[0]]

        for i in intervals[1:]:
            last = merged[-1]
            if i[0] <= last[-1]:
                last[-1] = max( i[-1], last[-1])
            else:
                merged.append(i)
        
        return merged



        