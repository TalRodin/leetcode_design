class RandomizedSet:
    def __init__(self):
        self.s=set()
    def insert(self, val):
        if val in self.s:
            return False
        self.s.add(val)
        return True
    def remove(self,val):
        if val not in self.s:
            return False
        self.s.remove(val)
        return True
    def getRandom(self):
        from random import randint
        return list(self.s)[randint(0,len(self.s)-1)]

obj=RandomizedSet()
print(obj.s)
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.insert(6)
print(obj.s)
obj.remove(1)
print(obj.getRandom())
    