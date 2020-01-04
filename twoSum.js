class TwoSum{
    constructor(){
        this.dict={}
    }
    add(number){
        if (number in this.dict){
            this.dict[number]+=1
        }
        else{
            this.dict[number]=1
        }
    }
    find(value){
        let r=this.dict
        for (let num in r){
            let left=value-num
            if ((left!==num && left in r ) || (left===num && r[num]>1)){
                return true
            }
            
        }
        return false
    }
}

obj=new TwoSum()
obj.add(4)
obj.add(5)
obj.add(4)
console.log(obj.find(7))