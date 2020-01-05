class MyQueue{
    constructor(){
        this.stack1=[]
    }
    push(val){
        this.stack1.push(val)
    }
    pop(){
        return this.stack1.shift()
    }
    peek(){
        let v=this.stack1.shift()
        this.stack1.unshift(v)
        return v
    }
    empty(){
        return this.stack1.length===0
    }
}

obj=new QueueUsingStack()
obj.push(1)
obj.push(2)
console.log(obj.peek())
console.log(obj.pop())
console.log(obj.stack1)



// ["MyQueue","push","push","peek","pop","empty"]
// [[],[1],[2],[],[],[]]


// [null,null,null,1,1,false]