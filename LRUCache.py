import collections
class LRUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache=collections.OrderedDict()
    def put(self,key,value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache)==self.capacity:
            self.cache.popitem(last=False)
        self.cache[key]=value
    def get(self, key):
        if not key in self.cache:
            return -1
        value=self.cache.pop(key)
        print(value)
        self.cache[key]=value
        return value

obj=LRUCache(4)
obj.put('a',4)
obj.put('b',3)
obj.put('c',9)
obj.put('b',7)
obj.put('d',8)
obj.put('e',6)
print(obj.cache)
print(obj.get('d'))
    