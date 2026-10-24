class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        Pmap = {'}':'{',')': '(',']':'['}

        for p in s:
            if p in Pmap:
                if stack and stack[-1] == Pmap[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return True if not stack else False
