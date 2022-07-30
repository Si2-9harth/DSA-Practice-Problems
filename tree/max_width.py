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
            return self.arr.pop(0)
    def size(self):
        return len(self.arr)

def width(root):
    if root==None:
        return 0
    else:
        q=queue()
        q.push(root)
        res=1
        while q.empty()==False:
            count=q.size()
            res=max(res,count)
            for i in range(count):
                c=q.pop()
                if c.left!=None:
                    q.push(c.left)
                if c.right!=None:
                    q.push(c.right)
        return res


root=Node(20)
n1=Node(8)
n2=Node(2)
n3=Node(5)
n4=Node(12)
n5=Node(0)
root.left=n1
root.right=n4
n1.left=n2
n1.right=n3
n4.left=n5
print(width(root))