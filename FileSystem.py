class FileSystem:
    def __init__(self):
        self.data={"":-1}
    def get(self, path):
        if path in  self.data:
            return self.data[path]
        return -1
    def createPath(self, path, value):
        if path[:path.rfind("/")] not in self.data or path in self.data:
            return False
        self.data[path]=value
        return True
    
counter=FileSystem()
counter.createPath("/a",1)
print(counter.data)
print(counter.get("/a"))
print(counter.data)
# ["FileSystem","createPath","get"]
# [[],["/a",1],["/a"]]
# Output: 
# [null,true,1]
# Explanation: 
# FileSystem fileSystem = new FileSystem();
# fileSystem.createPath("/a", 1); // return true
# fileSystem.get("/a"); // return 1