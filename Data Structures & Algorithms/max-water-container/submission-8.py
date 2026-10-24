class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxW = 0 
        l, r = 0, len(heights) - 1


        while l < r:
            water = (r-l) * min(heights[l], heights[r])
            maxW = max (maxW, water)
        
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxW
        