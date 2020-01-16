class ZigZagIterator{
    constructor(v1, v2){
        if (v1.length===0){
            temp=v1
            v1=v2
            v2=temp
        }
        this.currVec=v1
        this.nextVec=v2
        this.currIdx=0
        this.nextIdx=0
    }
    next(){
        let ret=this.currVec[this.currIdx]
        this.currIdx+=1
        if (this.nextIdx<this.nextVec.length){
            let temp=this.currVec
            this.currVec=this.nextVec
            this.nextVec=temp

            temp=this.currIdx
            this.currIdx=this.nextIdx
            this.nextIdx=temp
        }
        return ret
    }
    hasNext(){
        return this.currIdx<this.currVec.length
    }
}

v1 = [1, 2]
v2 = [3, 4, 5, 6]
obj=new ZigZagIterator(v1, v2)
console.log(obj.currVec)
console.log(obj.nextVec)
console.log(obj.currIdx)
console.log(obj.nextIdx)
i= new ZigZagIterator(v1, v2)
v=[]
while (i.hasNext()){
    v.push(i.next())
    console.log(v)
} 
    