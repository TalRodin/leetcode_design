# import collections
class TwoSum(object):
    def __init__(self):
        # self.record = collections.defaultdict(int)
        self.record={}
    def add(self, number):
        if number in self.record:
            self.record[number]+=1
        else:
            self.record[number]=1
    def find(self, value):
        r=self.record
        for num in r:
            left = value - num
            if left!=num and left in r or left == num and r[num]>1:
                return True
        return False
    
obj=TwoSum()
obj.add(4)
obj.add(5)
obj.add(4)
print(obj.find(8))