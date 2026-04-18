class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Two pointer: O(n+m) and O(1)
        i = j = 0 

        # before any reach its end check each character 
        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                # if match, both move on to the next
                i += 1
                j += 1
                # else, move s to the next to check again
            else:
                i += 1
        # once reach the end return the leftover character len
        return len(t) - j
                
        
        

        

        