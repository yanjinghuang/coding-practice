class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 
        l = 0
        r = len(heights) - 1 

        while l < r:
            min_h = min(heights[l], heights[r])
            area = (r-l) * min_h
            res = max(res, area)

            if heights[r] < heights[l]:
                r -= 1 
            else:
                l += 1 
        return res

        