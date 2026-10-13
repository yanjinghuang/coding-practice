class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:  # Greedy 
        intervals.sort(key=lambda x :x[1])
        prevEnd = intervals[0][1] #keep track previous end to compare
        res = 0

        for i in range(1 ,len(intervals)):
            if prevEnd > intervals[i][0]: #overlapped, drop the first one
                res += 1
            else:
                prevEnd = intervals[i][1] # no overlapped, up the prev end
        
        return res
