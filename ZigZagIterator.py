class ZigZagIterator():
    def __init__(self, v1, v2):
        if len(v1)==0:
            v1,v2=v2,v1
        self.currVec=v1
        self.nextVec=v2
        self.currIdx=0
        self.nextIdx=0
    def next(self):
        ret = self.currVec[self.currIdx]
        self.currIdx+=1
        if self.nextIdx<len(self.nextVec):
            self.currVec, self.nextVec = self.nextVec, self.currVec
            self.currIdx, self.nextIdx = self.nextIdx, self.currIdx
        return ret
    def hasNext(self):
        return self.currIdx<len(self.currVec)

v1 = [1, 2]
v2 = [3, 4, 5, 6]
obj=ZigZagIterator(v1, v2)
print(obj.currVec)
print(obj.nextVec)
print(obj.currIdx)
print(obj.nextIdx)
i, v = ZigZagIterator(v1, v2), []
while i.hasNext(): 
    v.append(i.next())
print(v)