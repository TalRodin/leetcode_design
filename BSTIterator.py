# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class BSTIterator:
    def __init__(self, root):
        self.q=[]  
        self.allLeft(root)
    def hasNext(self):
        return len(self.q) > 0
    def next(self):
        cur = self.q.pop()
        if cur.right:
            self.allLeft(cur.right)
        return cur.val
    def allLeft(self, root):
        while root:
            self.q.append(root)
            root = root.left


