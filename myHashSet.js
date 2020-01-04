class MyHashSet{
    constructor(n){
        this.array= []
    }
    bool(n){
        for (let i=0; i<n;i++){
            this.array.push(false)
        }
    }
    add(key){
        for (let i=0;i<this.array.length;i++){
            if (i===key){
                this.array[i]= true
            }
        }
        return this
    }
    remove(key){
        for (let i=0; i<this.array.length; i++){
            if(i===key){
                this.array[i]=false
            }
        }
        return this 
    }
    contains(key){
        return this.array[key]
    }
}

obj=new MyHashSet()
obj.bool(5)

console.log(obj.add(3))

console.log(obj.contains(3))