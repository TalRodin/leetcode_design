class ValidWordAbbr{
    constructor(dictionary){
        this.abbrev={}
        this.dictionary=new Set(dictionary)
       
        for (let i=0;i<dictionary.length;i++){
            let  abb=this.process(dictionary[i])
            if (abb in this.abbrev){
                this.abbrev[abb]+=1
            }else{
                this.abbrev[abb]=1
            }
        }
    }
    process(word){
        if (word.length<=2) {
            return word}else{
        return (word[0]+(word.length-2)+word[word.length-1])
        }
    }
    isUnique(word){
       
        if ((this.dictionary.has(word) && this.abbrev[this.process(word)]==1) || !(this.abbrev[this.process(word)])){
            return true
        }else{
            return false
        }
    }
}
// return (word in self.dictionary and self.abbrev[self.process(word)]==1 or not self.process(word) in self.abbrev)
obj=new ValidWordAbbr([ "deer", "door", "cake", "card" ])
console.log(obj.abbrev)
console.log(obj.dictionary)
console.log(obj.isUnique('deer'))