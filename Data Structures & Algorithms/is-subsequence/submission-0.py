class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Two pointer 
        # Initiate first 
        i = j = 0
        while i < len(s) and j < len(t):
            # Only increment if found
            if s[i] == t[j]:
                i += 1
            # Increment j every time 
            j += 1
        return i == len(s)  # true if it is at the last char of s
            

        



    

        