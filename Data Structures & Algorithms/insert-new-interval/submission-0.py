class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    ##1. No overlapped 
    ##       end is before first start - insert before
    ##      start is after the last end - insert after 
    #3. if overllap - merge  """

        res = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            else:
                newInterval = [min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1])
                ] # merge/widen the interval, keep going 
                
        res.append(newInterval)
            
        return res




