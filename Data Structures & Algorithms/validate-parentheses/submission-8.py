class Solution:
    def isValid(self, s: str) -> bool:
        # match pairs, in order
        # stack only care about the most recent things 

        # append the left and pop if it is a match

        stack = []
        c_map = {
                '(' :')',
                '{': '}',
                '[': ']'
                }

        for c in s:
            if c in c_map:
                stack.append(c)
            else:
                # not match 
                if not stack or c != c_map[stack[-1]]:
                    return False 

                # match 
                stack.pop()
                
        return not stack
