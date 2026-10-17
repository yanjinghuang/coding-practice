class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}

        for i in range(len(s)):
            s_ch, t_ch = s[i], t[i]
            if (s_ch in sMap and sMap[s_ch] != t_ch) or (t_ch in tMap and tMap[t_ch] != s_ch):
                return False 

            sMap[s_ch] = t_ch
            tMap[t_ch] = s_ch
        
        return True 





        