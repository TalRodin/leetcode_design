class leaderBoard{
    constructor(){
        this.hmap={}
    }
    addScore(playerID, score){
        if (playerID in this.hmap){
            this.hmap[playerID]+=parseInt(score)
        }
        else{
            this.hmap[playerID]=parseInt(score)
        }   
    }
    top(k){
        let total=0
        let q=Object.values(this.hmap)
        let arr=[]
        for (let i=0;i<k;i++){
            let m=Math.max(...q)
            arr.push(m)
            q.splice(q.indexOf(m),1)
        }
        total=arr.reduce((a,b) => a + b, 0)
        return total

    }
    reset(playerID){
        this.hmap[playerID]=0
    }
    
}

obj=new leaderBoard()
obj.addScore(1,5)
obj.addScore(2,6)
obj.addScore(4,6)
obj.addScore(6,2)
obj.addScore(4,14)
obj.addScore(6,30)
console.log(obj.hmap)
console.log(obj.hmap)
console.log(obj.top(2))
console.log(obj.hmap)
console.log(obj.top(3))