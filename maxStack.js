class maxStack{
    constructor(){
        this.stack=[]
        this.max_v=[-Infinity]
    }
    push(x){
        this.stack.push(x)
        this.max_v.push(Math.max(x,this.max_v[this.max_v.length-1]))
    }
    pop(){
        this.stack.pop()
        this.max_v.pop()
    }
    top(){
        return this.stack[this.stack.length-1]
    }
    getMax(){
        return this.max_v[this.max_v.length-1]
    }
}



obj=new maxStack()
console.log(obj.stack)
obj.push(34)
obj.push(5)
obj.push(90)
obj.push(67)
obj.push(34)
obj.push(28)
console.log(obj.stack)
console.log(obj.max_v)
obj.pop()
console.log(obj.max_v)
console.log(obj.stack)
console.log(obj.top())
console.log(obj.getMax())