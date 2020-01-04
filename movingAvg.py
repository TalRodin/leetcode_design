class MovingAverage(object):
    def __init__(self, size):
        self.size=size
        self.queue=[]
    def next(self,val):
        if not self.queue or len(self.queue)<self.size:
            self.queue.append(val)
        elif len(self.queue)==self.size:
            self.queue.pop(0)
            self.queue.append(val)
            return (float(sum(self.queue))/len(self.queue))
        return ('Append more values')

obj=MovingAverage(5)
print(obj.next(4))
print(obj.queue)
print(obj.next(9))
print(obj.queue)
print(obj.next(2))
print(obj.queue)
print(obj.next(9))
print(obj.queue)
print(obj.next(4))
print(obj.queue)
print(obj.next(0))