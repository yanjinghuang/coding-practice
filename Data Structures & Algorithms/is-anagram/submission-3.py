class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        for ch in s:
            if ch not in s_dict:
                s_dict[ch] = 1
            else:
                 s_dict[ch] += 1
        
        for a in t:
            if a not in s_dict:
                return False
            s_dict[a] -= 1
            if s_dict[a] < 0:
                return False
        return True 