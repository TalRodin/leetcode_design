class minStack:
    def __init__(self):
        self.stack=[]
        self.min_v=[float('inf')]
    def push(self,x):
        self.stack.append(x)
        self.min_v.append(min(x,self.min_v[-1]))
    def pop(self):
        self.min_v.pop()
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.min_v[-1]
obj=minStack()
obj.push(34)
obj.push(5)
obj.push(90)
obj.push(67)
obj.push(34)
obj.push(28)
print(obj.min_v)
obj.pop()
print(obj.min_v)
print(obj.stack)
print(obj.top())
print(obj.getMin())
