class BSTIterator{
    constructor(root){
        this.q=[]
        this.allLeft(root)
    }
    hasNext(){
        return this.q.length>0
    }
    next(){
        let cur=this.q.pop()
        if(cur.right){
            this.allLeft(cur.right)
        }
        return cur.val
    }
    allLeft(root){
        while (root){
            this.q.push(root)
            root=root.left
        }
    }
}