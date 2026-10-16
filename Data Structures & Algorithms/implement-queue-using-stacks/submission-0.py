class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack_temp = [] # temp
        

    def push(self, x: int) -> None:
        self.stack.append(x)


    def pop(self) -> int:
        if not self.stack_temp:
            while self.stack:
                self.stack_temp.append(self.stack.pop())
        return self.stack_temp.pop()

    def peek(self) -> int:
        if not self.stack_temp:
            while self.stack:
                self.stack_temp.append(self.stack.pop())
        return self.stack_temp[-1]
        

    def empty(self) -> bool:
        return max(len(self.stack), len(self.stack_temp)) == 0 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()