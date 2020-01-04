class StackUsingQueue{
    constructor(){
        this.q=[]
    }
    push(x){
        this.q.push(x)
        for(let i=0;i<this.q.length-1;i++){
            this.q.push(this.q.shift())
        }
    }
    pop(){
        return this.q.shift()
    }
    top(){
        return this.q[0]
    }
    empty(){
        return !this.q.length
    }  
}

obj=new StackUsingQueue()
obj.push(1)
obj.push(4)
obj.push(5)
obj.push(7)
console.log(obj.q)
obj.pop()
console.log(obj.q)
console.log(obj.top())

console.log(obj.empty())