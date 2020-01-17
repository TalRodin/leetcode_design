class RandomizedSet{
    constructor(){
        this.s=new Set
    }
    insert(val){
        if (Array.from(this.s).includes(val)){
            return false
        }
        this.s.add(val)
        return true
    }
    remove(val){
        if (!Array.from(this.s).includes(val)){
            return false
        }
        this.s.delete(val)
        return true
    }
    getRandom(){
        return Array.from(this.s)[Math.floor(Math.random() * this.s.size)]
    }
}

obj=new RandomizedSet()
console.log(obj.s)
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.insert(6)
console.log(obj.s)
obj.remove(1)
console.log(obj.s)
console.log(obj.getRandom())