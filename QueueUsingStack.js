class QueueUsingStack{
    constructor(){
        this.stack1=[]
        this.stack2=[]
    }
    push(val){
        this.stack1.push(val)
    }
    pop(){
        for (let i; i<this.stack1.length-1; i++){
            v=this.stack1.pop()
            this.stack2.push(v)
        }
        res=this.stack2.pop()
        for (let i; i<this.stack2.length;i++){
            v=this.stack2.pop()
            this.stack1.push(v)
        }
    }
    peek(){
        for (let i; i<this.stack1.length-1;i++){
            v=this.stack1.pop()
            this.stack2.push(v)
        }
        res=this.stack2[0]
        for (let i; i<this.stack2.length;i++){
            v=this.stack2.pop()
            this.stack1.push(v)
        }
    }
}

obj=new QueueUsingStack()
obj.push(4)
obj.push(5)
obj.push(3)
print(obj.stack1)