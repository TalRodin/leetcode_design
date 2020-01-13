class MinStack{
    constructor(){
        this.stack=[]
        this.min_v=[Infinity]
    }
    push(x){
        this.stack.push(x)
        this.min_v.push(Math.min(x,this.min_v[this.min_v.length-1]))
    }
    pop(){
        this.stack.pop()
        this.min_v.pop()
    }
    top(){
        return this.stack[this.stack.length-1]
    }
    getMin(){
        return this.min_v[this.min_v.length-1]
    }
}


obj=new MinStack()
console.log(obj.stack)
obj.push(34)
obj.push(5)
obj.push(90)
obj.push(67)
obj.push(34)
obj.push(28)
console.log(obj.stack)
console.log(obj.min_v)
obj.pop()
console.log(obj.min_v)
console.log(obj.stack)
console.log(obj.top())
console.log(obj.getMin())
