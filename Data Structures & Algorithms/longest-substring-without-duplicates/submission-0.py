class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} # ch : idx
        left = 0 
        best = 0

        for right in range(len(s)):
            ch = s[right]
            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1
            seen[ch] = right 
            best = max(best, right - left + 1)

        return best