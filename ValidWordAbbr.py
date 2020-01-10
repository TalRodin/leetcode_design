from collections import defaultdict
class ValidWordAbbr:
    def __init__(self, dictionary):
        self.abbrev=defaultdict(int)
        self.dictionary=set(dictionary)
        for word in dictionary:
            self.abbrev[self.process(word)]+=1
    def process(self, word):
        if len(word)<=2:
            return word
        return word[0]+str(len(word)-2)+word[-1]
    def isUnique(self, word):
        return (word in self.dictionary and self.abbrev[self.process(word)]==1 or not self.process(word) in self.abbrev)


obj=ValidWordAbbr([ "deer", "door", "cake", "card" ])
print(obj.abbrev)
print(obj.dictionary)
print(obj.isUnique('cake'))

