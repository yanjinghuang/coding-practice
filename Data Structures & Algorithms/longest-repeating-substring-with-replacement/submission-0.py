class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #  # of replacement = len(cur_substring) - most freq char
        # sliding window (l, r) -> # of most freq -> number replacement <> k


        counter = {} # ch : count 
        maxf = 0 
        res = 0
        l = 0 

        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            maxf = max(maxf, counter[s[r]])
        
            while (r - l + 1) - maxf > k:  
                counter[s[l]] -= 1  # decrement the count
                l += 1  # move the left counter forward
            
            res = max(res, r - l + 1) # check current substring 

        
        return res


