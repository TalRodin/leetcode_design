class MyQueue():
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self,val):
        self.stack1.append(val)
    def pop(self):
        for i in range(len(self.stack1)-1):
            v=self.stack1.pop()
            self.stack2.append(v)
        res= self.stack1.pop()
        for i in range(len(self.stack2)):
            v=self.stack2.pop()
            self.stack1.append(v)
        return res
    def peek(self):
        for i in range(len(self.stack1)-1):
            v=self.stack1.pop()
            self.stack2.append(v)
        res= self.stack1[0]
        for i in range(len(self.stack2)):
            v=self.stack2.pop()
            self.stack1.append(v)
        return res
    def empty(self):
        return len(self.stack1)==0

obj=Queue_using_Stack()
print(obj.stack1)
obj.push(4)
obj.push(5)
obj.push(3)
obj.push(2)
obj.pop()
print(obj.stack1)
print(obj.peek())