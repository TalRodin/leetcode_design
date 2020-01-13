class PhoneDirectory{
    constructor(maxNumber){
        this.curr=0
        this.numbers=[]
        this.used=[]
        for(let i=0;i<maxNumber;i++){
            this.numbers.push(i)
            this.used.push(false)
        }
    }
    get(){
        if(this.curr==this.numbers.length){
            return -1
        }
        let number= this.numbers[this.curr]
        this.curr+=1
        this.used[number]=true
        return number
    }
    check(number){
        return (0<=number && number<this.numbers.length) && (!this.used[number])
    }
    release(number){
        if(this.used[number]){
            this.curr-=1
            this.numbers[this.curr]=number
            this.used[number]=false
        }
    }
}

obj=new PhoneDirectory(5)
console.log(obj.numbers)
console.log(obj.get())
console.log(obj.used)
console.log(obj.get())
console.log(obj.used)
console.log(obj.check(1))
obj.release(1)
console.log(obj.check(1))