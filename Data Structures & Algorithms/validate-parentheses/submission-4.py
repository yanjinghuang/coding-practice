class Solution:
    def isValid(self, s: str) -> bool:
        # match pairs, in order
        # only care about the most recent things 

        stack = []
        c_map = { '(' : ')',
                  '{' : '}',
                  '[': ']'}

        for c in s:
            if c in c_map:
                stack.append(c)
            else:
                if not stack or c_map[stack[-1]] != c:
                    return False
                stack.pop()
        
        return not stack 
                    
        




        