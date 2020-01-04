class NestedIterator(object):
    def __init__(self, nestedList):
        self._depth = [[nestedList, 0]]
    def next(self):
        nestedList, i = self._depth[-1]
        print(nestedList)
        self._depth[-1][1] += 1
        return nestedList[i].getInteger()
    # def hasNext(self):
    #     while self.__depth:
    #         nestedList, i = self.__depth[-1]
    #         if i == len(nestedList):
    #             self.__depth.pop()
    #         elif nestedList[i].isInteger():
    #                 return True
    #         else:
    #             self.__depth[-1][1] += 1
    #             self.__depth.append([nestedList[i].getList(), 0])
    #     return False

n=[[1,1],2,[1,1]]
obj=NestedIterator(n)
print(obj.next)