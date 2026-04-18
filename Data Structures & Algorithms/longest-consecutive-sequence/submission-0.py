class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the start of sequence -> if an only if num-1 does not exist 
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # if it is the start num
            if (n-1) not in numSet:
                length = 0 
                while (n + length) in numSet:
                    length += 1 
                
                longest = max(longest,length)
        return longest

    
        