from collections import defaultdict
class WordDictionary:
    def __init__(self):
        self.words = defaultdict(set)
    def addWord(self, word):
        self.words[len(word)].add(word)
        
    def search(self, word):
        for i in self.words[len(word)]:
            for x,c in enumerate(word):
                print(i[x])
                if c not in ['.',  i[x]]:
                    break
            # any_mismatch = any(word[x] != '.' and word[x] != i[x]  for x in range(len(word)))
                else:
                    return True
        return False
		       
    
obj=WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
obj.addWord("hello")
print(obj.words)
print(obj.search("pad"))
print(obj.search("bad"))
print(obj.search(".ad"))
print(obj.search("b.."))

