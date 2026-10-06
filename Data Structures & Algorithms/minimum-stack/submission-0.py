class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        if not self.stack:
            mini=val
        else:
            mini=self.stack[-1]
        self.stack.append(val)
        if val<mini:
            mini=val
        self.stack.append(mini)
    def pop(self) -> None:
        self.stack.pop(-1)
        self.stack.pop(-1)
    def top(self) -> int:
        return self.stack[-2]
        
    def getMin(self) -> int:
        return self.stack[-1]
        
