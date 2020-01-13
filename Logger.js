class Logger{
    constructor(){
        this.data={}
    }
    shouldPrintMessage(timestamp, message){
       if (!Object.keys(this.data).includes(message) || (timestamp-this.data[message]>=10)){
            this.data[message]=timestamp
            return true
       }else{
           return false
       }
    }
}


obj=new Logger()
console.log(obj.data)
console.log(obj.shouldPrintMessage(1, "foo"))
console.log(obj.shouldPrintMessage(2,"bar"))
console.log(obj.shouldPrintMessage(3,"foo"))