class hitCounter:
    def __init__(self):
        self.data=[]
    def hit(self, timestamp):
        self.data.append(timestamp)
    def getHits(self, timestamp):
        while self.data and int(timestamp)-self.data[0]>=300:
            self.data.pop(0)
        return len(self.data)
obj=hitCounter()
obj.hit(1)
obj.hit(10)
obj.hit(20)
obj.hit(30)
obj.hit(120)
obj.hit(130)
obj.hit(230)
obj.hit(300)
obj.hit(301)
obj.hit(302)
print(obj.getHits('130'))
print(obj.data)
