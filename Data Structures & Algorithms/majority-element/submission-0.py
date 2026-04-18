class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cutoff = len(nums) // 2
        cnt_set = defaultdict(int)

        for n in nums:
            cnt_set[n] += 1 

        for e, cnt in cnt_set.items():
            if cnt > cutoff:
                return e 
            