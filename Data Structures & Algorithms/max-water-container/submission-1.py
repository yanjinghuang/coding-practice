class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights)-1 
        maxP = 0

        while l < r:
            product = (r-l) * min(heights[l], heights[r])
            maxP = max(product, maxP)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxP



        