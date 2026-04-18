class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(n), O(n)
        # cutoff = len(nums) // 2 

        # cnt_dict = defaultdict(int)

        # for n in nums:
        #     cnt_dict[n] += 1 

        
        # for n, cnt in cnt_dict.items():
        #     if cnt > cutoff:
        #         return n 
        
        #  O(n), O(1) -> Boyer Moore Voting, pair and cancel out, what left is the majority 

        count = 0 
        candidate = None 

        for n in nums:
            if count == 0:
                candidate = n
            count += (1 if n == candidate else -1)
        
        return candidate 
        
  
