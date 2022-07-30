class Node:
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None

class queue:
    def __init__(self):
        self.arr=[]
    def empty(self):
        return self.arr==[]
    def push(self,val):
        self.arr.append(val)
    def pop(self):
        if self.empty():
            return
        else:
            return self.arr.pop()
    def size(self):
        return len(self.arr)

def iter(root):
    if root==None:
        return float('-inf')
    else:
        q=queue()
        res=float('-inf')
        q.push(root)
        while q.empty()==False:
            c=q.pop()
            res=max(res,c.key)
            if c.left!=None:
                q.push(c.left)
            if c.right!=None:
                q.push(c.right)
        return res


def rec(root):
    if root==None:
        return float('-inf')
    else:
        return max(root.key,max(rec(root.left),rec(root.right)))
    

root=Node(10)
n1=Node(20)
n2=Node(30)
n3=Node(40)
n4=Node(50)
root.left=n1
root.right=n2
n2.left=n3
n2.right=n4
print(rec(root))
print(iter(root))