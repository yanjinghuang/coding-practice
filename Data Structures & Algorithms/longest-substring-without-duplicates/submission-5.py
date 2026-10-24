class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        l = 0
        res = 0
        seen = {}

        for r in range(len(s)):
            ch = s[r]
            if ch in seen:
                l = max(l, seen[ch] + 1)
            seen[ch] = r
            res = max( res, r - l + 1 )

        return res
