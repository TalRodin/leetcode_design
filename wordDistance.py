import collections
class WordDistance:
    def __init__(self, words):
        self.wordIndex=collections.defaultdict(list)
        for i in range (len(words)):
            self.wordIndex[words[i]].append(i)
    def shortest(self, word1, word2):
        indexes1=self.wordIndex[word1]
        indexes2=self.wordIndex[word2]
        i,j,dist=0,0,float('inf')
        while i<len(indexes1) and j<len(indexes2):
            n=indexes1[i]
            m=indexes2[j]
            if(n<m):
                dist=min(dist, m-n)
                i+=1
            else:
                dist=min(dist, n-m)
                j+=1
        return dist
obj=WordDistance(['hello','worldhello', 'you'])
print(obj.shortest('hello', 'you'))
print(obj.wordIndex)