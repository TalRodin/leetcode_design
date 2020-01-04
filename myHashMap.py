class MyHashMap(object):
    def __init__(self):
        self.dict={}
    def put(self, key, val):
        if key not in self.dict:
            self.dict[key]=val
    def get(self,key):
        if key in self.dict:
            return self.dict[key]
        else:
            return -1
    def remove(self, key):
        if key in self.dict:
            del self.dict[key]
        else:
            return -1

obj = MyHashMap()
obj.put('a', 4)
obj.put('b', 5)
obj.put('c', 3)
obj.put('d', 2)
obj.put('e', 8)

print(obj.get('d'))
print(obj.get('f'))
print(obj.remove('d'))
print(obj.get('d'))