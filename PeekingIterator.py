class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.temp=''
        if self.iter.hasNext():
            self.temp=self.iter.next()
        else:
            self.temp = None
    def peek(self):
        return self.temp

    def next(self):
        ret = self.temp
        if self.iter.hasNext():
            self.temp = self.iter.next()
        else:
            self.temp = None
        return ret

    def hasNext(self):
        if self.temp != None:
            return True
        else:
            return False

obj = PeekingIterator([1,2,3])

print(obj.peek())



