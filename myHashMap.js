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
             delete this.dict.key
        }
        else{
            return -1
        }
    }
}

obj=new MyHashMap()
obj.put('q',5)
console.log(obj.dict)
console.log(obj.remove('q'))