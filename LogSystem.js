class LogSystem{
    constructor(){
        this.logs=[]
        this.granularity={'Year':4, 'Month':7, 'Day':10, 'Hour':13, 'Minute':16, 'Second': 19}
    }
    put(id, timestamp){
        this.logs.push((id, timestamp))
    }
    retrieve(s,e,gra){
        let i=this.granularity[gra]
        console.log(i)
        let begin=s.slice(0,i)
        let end=e.slice(0,i)
        let arr=[]
        for (let j=0; j<this.logs.length;j++){
            console.log(this.logs[j].slice(0,i))
            if (begin<=this.logs[j].slice(0,i) && end>=this.logs[j].slice(0,i)){
                arr.push(j)
            }
        }
        return arr.sort()
    }
}

obj=new LogSystem()
console.log(obj.granularity)
obj.put(1, "2017:01:01:23:59:59")
obj.put(2, "2017:01:01:22:59:59")
obj.put(3, "2016:01:01:00:00:00")
console.log(obj.logs)

console.log(obj.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"))
console.log(obj.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"))
