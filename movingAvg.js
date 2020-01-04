class MovingAverage{
    constructor(size){
        this.size=size
        this.queue=[]
    }
    next( val){
        if(this.queue.length<this.size){
            this.queue.push(val)
            return 'append more values'

        }
        else if(this.queue.length>=this.size){
            this.queue.shift()
            this.queue.push(val)
            return (this.queue.reduce((acc, curV) => acc+curV, 0)/this.queue.length)
        
}}
}
obj=new MovingAverage(5)
obj.next(3)
console.log(obj.queue)
obj.next(34)
console.log(obj.queue)
obj.next(36)
console.log(obj.queue)
obj.next(33)
console.log(obj.queue)

console.log(obj.next(2))

console.log(obj.next(23))

console.log(obj.next(29))