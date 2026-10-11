class Solution:
    def trap(self, height: List[int]) -> int:
        #  trap is = shorter wall 
        #  water[i] = min(maxL and maxR) - height[i]
        # which is the shorter, move the shorter pointer and get new max and calcualt different

        if not height: return 0 

        res = 0
        l, r = 0, len(height)-1
        Lmax, Rmax = height[l], height[r]

        while l < r:
            if Lmax < Rmax:
                l += 1
                Lmax = max(Lmax, height[l])
                res += Lmax - height[l]
            else:
                r -= 1 
                Rmax = max(Rmax, height[r])
                res += Rmax - height[r]
        
        return res