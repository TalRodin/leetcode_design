class hitCounter{
    constructor(){
        this.data=[]
    }
    hit(timestamp){
        this.data.push(timestamp)
    }
    getHits(timestamp){
        while (this.data && (timestamp-this.data[0])>=300){
            this.data.shift()
        }
        return this.data.length
    }
}
obj=new hitCounter()
obj.hit(1)
obj.hit(10)
obj.hit(20)
obj.hit(30)
obj.hit(120)
obj.hit(130)
obj.hit(230)
obj.hit(300)
obj.hit(301)
obj.hit(302)
console.log(obj.getHits('130'))
console.log(obj.data)