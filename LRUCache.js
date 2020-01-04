class LRUCache{
    constructor(capacity){
        this.capacity=capacity
        this.cache={}
    }
    set(key, value){
        console.log(Object.keys(this.cache).length)
        if (key in this.cache){
            delete this.cache[key]
        }
        else if(Object.keys(this.cache).length===this.capacity){
            delete this.cache[Object.keys(this.cache)[0]]   
        }
        this.cache[key]=value
    }
    get(key){
        if (key in this.cache){
            let value = this.cache[key] //40
            delete this.cache[key]
            this.cache[key]=value
            return value
        }
        else{
            return -1
        }
    }
}

obj=new LRUCache(4)
obj.set('c', 9)
obj.set('a', 4)
obj.set('b', 7)
obj.set('e', 6)
obj.set('e', 90)
obj.set('f', 40)
obj.set('r', 50)
console.log(obj.cache)
console.log(obj.get('f'))
console.log(obj.cache)