class Solution:
    def trap(self, height: List[int]) -> int:
        # min (max_l, max_r) - h[i]
        l, r = 0, len(height)-1
        area = 0

        max_l = height[l]
        max_r = height[r]

        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                area += (max_l - height[l])
            
            else:
                r -= 1
                max_r = max(max_r, height[r])
                area += (max_r - height[r])
        return area

    

       