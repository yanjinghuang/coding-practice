class Solution:
    def check(self, nums: List[int]) -> bool:
        # 1. if more than 1 breaking point; fail
        # 2. compare cur num with rotated nums i+1

        N = len(nums)
        count = 0 

        for i in range(N):
            if nums[i] > nums[(i + 1) % N]:
                count += 1 
                if count > 1:
                    return False
        
        return True