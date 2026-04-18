class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.split().pop())

        # Iteration
        i = len(s)-1 
        length = 0

        while s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            i -= 1 
            length += 1
        return length
        


        