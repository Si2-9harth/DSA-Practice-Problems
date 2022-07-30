class Node:
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None

class stack:
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

def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)

def iterative(root):
    s=stack()
    cur=root
    while cur!=None or s.empty()==False:
        while cur!=None:
            s.push(cur)
            cur=cur.left
        c=s.pop()
        print(c.key,end=" ")
        cur=c.right

root=Node(10)
n1=Node(20)
n2=Node(30)
n3=Node(40)
n4=Node(50)
root.left=n1
root.right=n2
n2.left=n3
n2.right=n4
inorder(root)
print()
iterative(root)