class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}  # {ch, inx}
        l = 0
        res = 0

        for r in range(len(s)):
            ch = s[r]

            if ch in seen:
                l = max(l, seen[ch] + 1)
            
            seen[ch] = r
            res  = max(res, r- l + 1)
        
        return res
