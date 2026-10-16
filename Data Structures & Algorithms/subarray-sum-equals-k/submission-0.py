class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Hashmap [frequency] + prefix 
        freq = {0:1}
        # sum up to that point 
        prefix = 0
        count = 0


        for n in nums:
            prefix += n
            
 # Get diff, increment by the frequency of the diff, otherwise 0
            count += freq.get(prefix - k, 0)

# increment the prefix freq
            freq[prefix] = freq.get(prefix, 0) + 1 
        
        return count

                