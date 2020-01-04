class MyHashSet(object):
    def __init__(self,n):
        self.array=[False]*n
    def add(self,key):
        self.array[key]=True
    def remove(self,key):
        self.array[key]=False
    def contains(self, key):
        return self.array[key]
obj=MyHashSet(10)
print(obj.array)
obj.add(4)
obj.add(3)
print(obj.array)
obj.remove(4)
print(obj.array)

print(obj.contains(3))

    
