class FileSystem{
    constructor(){
        this.data={'':-1}
    }
    get(path){
        if(path in this.data){
            return this.data[path]
        }else{
            return -1
        }
    }
    createPath(path, value){
        if (!(path.slice(0,path.search("/")) in this.data) || (path in this.data)){
            return false
        }
        this.data[path]=value
        return true
    }
}


obj= new FileSystem()
console.log(obj.data)
obj.createPath("/a",1)
console.log(obj.data)
console.log(obj.get("/a"))