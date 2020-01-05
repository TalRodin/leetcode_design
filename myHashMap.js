class MyHashMap{
    constructor(){
        this.dict={}
    }
    put(key, val){
        this.dict[key]=val
    }
    get(key){
        if(key in this.dict){
           return this.dict[key] 
        }
        else{
            return  -1}
     }
    remove(key){
        if(key in this.dict){
             delete this.dict[key]
        }
        else{
            return -1
        }
    }
}

obj=new MyHashMap()
obj.put(1,1)
obj.put(2,2)
console.log(obj.get(1))
console.log(obj.get(3))
obj.put(2,1)
console.log(obj.dict)
obj.remove(2)
console.log(obj.dict)
console.log(obj.get(2))

// ["MyHashMap","put","put","get","get","put","get", "remove", "get"]
// [[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]

// [null,null,null,1,-1,null,1,null,-1]