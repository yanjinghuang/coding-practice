class Solution:
    def trap(self, height: List[int]) -> int:
        # min (max_l, max_r) - h[i]

        l = 0 
        r = len(height) - 1

        max_l = height[l]
        max_r = height[r]

        area = 0 



        while l < r:
            if max_l < max_r:
                l += 1 
                max_l = max(height[l], max_l)
                area += (max_l - height[l])
            else:
                r -=1 
                max_r = max(height[r], max_r)
                area += (max_r - height[r])
        return area
            

            



    

        