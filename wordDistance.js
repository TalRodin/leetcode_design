class WordDistance{
    constructor(words){
        console.log(words)
        this.wordIndex={}
        for (let i=0; i<words.length; i++){
            this.wordIndex[words[i]]=[i]
        }
    }
    shortest(word1, word2){
        let indexes1=this.wordIndex[word1]
        let indexes2=this.wordIndex[word2]
        let i=0
        let j=0
        let dist=[Infinity]
        while (i<indexes1.length && j<indexes2.length){
            let n=indexes1[i]
            let m=indexes2[j]
            if(n<m){
                dist=Math.min(dist, m-n)
                i+=1
            }
            else{
                dist=min(dist, m-n)
                j+=1
            }
        }
        return dist
    }
}

obj=new WordDistance(['hello','worldhello', 'you'])
console.log(obj.wordIndex)
console.log(obj.shortest('hello', 'worldhello'))
