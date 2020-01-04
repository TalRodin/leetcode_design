import collections
class LRUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache=collections.OrderedDict()
    def _set(self,key,value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache)==self.capacity:
            self.cache.popitem(last=False)
        self.cache[key]=value
    def _get(self, key):
        if not key in self.cache:
            return -1
        value=self.cache.pop(key)
        print(value)
        self.cache[key]=value
        return value

obj=LRUCache(4)
obj._set('a',4)
obj._set('b',3)
obj._set('c',9)
obj._set('b',7)
obj._set('d',8)
obj._set('e',6)
print(obj.cache)
print(obj._get('d'))
    