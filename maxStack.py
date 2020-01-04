class maxStack:
    def __init__(self):
        self.stack=[]
        self.max_v=[float('-inf')]
    def push(self,x):
        self.stack.append(x)
        self.max_v.append(max(x,self.max_v[-1]))
    def pop(self):
        self.max_v.pop()
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def getMax(self):
        return self.max_v[-1]
obj=maxStack()
obj.push(34)
obj.push(5)
obj.push(90)
obj.push(67)
obj.push(34)
obj.push(28)
print(obj.max_v)
obj.pop()
print(obj.max_v)
print(obj.stack)
print(obj.top())
print(obj.getMax())