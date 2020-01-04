import collections
class leaderBoard:
    def __init__(self):
        self.hmap=collections.Counter()
    def addScore(self,playerID, score):
        if playerID not in self.hmap:
            self.hmap[playerID]=score
        else:
            self.hmap[playerID]+=score
    def top(self,k):
        i=0
        total=0
        for key, value in self.hmap.most_common(k):
            total+=value
        return total
    def reset(self, playerID):
        self.hmap[playerID]=0

obj=leaderBoard()
obj.addScore(1,5)
obj.addScore(2,6)
obj.addScore(4,6)
obj.addScore(6,2)
obj.addScore(4,4)
print(obj.hmap)
print(obj.top(2))
print(obj.reset)
