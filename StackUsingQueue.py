import collections
class StackUsingQueue:
    def __init__(self):
        self.queue =collections.deque()
    def push(self, x):
        self.queue.append(x)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
    def pop(self):
        return self.queue.popleft()
    def top(self):
        return self.queue[0]
    def empty(self):
        return not len(self.queue)
obj=StackUsingQueue()
obj.push(4)
obj.push(5)
obj.push(6)
print(obj.queue)
print(obj.pop())
print(obj.top())
obj.empty()
print(obj.queue)
obj.push(9)
print(obj.queue)