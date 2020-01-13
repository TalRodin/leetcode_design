class PhoneDirectory:
    def __init__(self, maxNumbers):
        self.curr=0
        self.numbers=[i for i in range(maxNumbers)]
        self.used=[False]*maxNumbers
    def get(self):
        if self.curr==len(self.numbers):
            return -1
        number=self.numbers[self.curr]
        self.curr+=1
        self.used[number]=True
        return number
    def check(self, number):
        return 0<=number<len(self.numbers) and not self.used[number]
    def release(self, number):
        if(self.used[number]):
            self.curr-=1
            self.numbers[self.curr] = number
            self.used[number]=False
            
obj=PhoneDirectory(5)
print(len(obj.numbers))
print(obj.get())

print(obj.used)
print(obj.get())

print(obj.used)
print(obj.check(1))
obj.release(1)
print(obj.check(1))
