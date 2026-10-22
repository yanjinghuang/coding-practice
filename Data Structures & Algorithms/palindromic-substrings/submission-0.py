class Solution:
    def countSubstrings(self, s: str) -> int:
        # two pointer O(n*2)
        res = 0 

        for i in range(len(s)):
            res += self.getP(s, i, i) # odd
            res += self.getP(s, i, i + 1)
        
        return res


    def getP(self, s, l, r):
        count = 0 
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1 
            r += 1
        
        return count

        