class WordDictionary{
    constructor(){
        this.words={}
    }
    addWord(word){
        
        if (word.length in this.words){
            this.words[word.length].add(word)
        }
        else{
            this.words[word.length]=new Set()
            this.words[word.length].add(word)
        }
    }
    search(word){
        
        for (let i=0;i<Array.from(this.words[word.length]).length; i++){
            for (let j in word){
               
                if (!['.',  i[j]].includes(word[j])){
                    
                    break
                }
                else{
                    return true
                }
             }
        }
        return false
    }
}

obj=new WordDictionary()
console.log(obj.words)
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
obj.addWord("hello")
console.log(obj.words)
console.log(obj.search("pad"))
console.log(obj.search("bad"))
console.log(obj.search(".ad"))
console.log(obj.search("b.."))