class Solution:
    def calculate(self, s: str) -> int:
        stack = [] 
        s = s.replace(' ', '')
        num = 0
        op = '+' #prev operator


        for c in (s + '+'):
            if c.isdigit():
                num = num * 10 + int(c)
            
            elif c in '+-/*':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '/':
                    stack.append( int(stack.pop() / num)) 
                else:
                    stack.append( stack.pop() * num) 

                num = 0
                op = c
        
        return sum(stack)




            
        

