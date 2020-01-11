import collections
class Logger:
    timeStoreLen=10
    def __init__(self):
        self.data=dict()
    def shouldPrintMessage(self, timestamp, message):
        if message not in self.data or timestamp-self.data[message]>=self.timeStoreLen:
            self.data[message]=timestamp
            return True
        else:
            return False

obj=Logger()
print(obj.data)
print(obj.shouldPrintMessage(1, "foo"))
print(obj.shouldPrintMessage(2,"bar"))
print(obj.shouldPrintMessage(3,"foo"))
print(obj.data)