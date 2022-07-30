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

def preorder(root):
    if root!=None:
        print(root.key,end=" ")
        preorder(root.left)
        preorder(root.right)

def iterative(root):
    s=stack()
    cur=root
    while cur!=None or s.empty()==False:
        while cur!=None:
            s.push(cur)
            print(cur.key,end=" ")
            cur=cur.left
        c=s.pop()
        cur=c.right

def iterativee(root):
    s=stack()
    cur=root
    s.push(cur)
    while s.empty()==False:
        c=s.pop()
        print(c.key,end=" ")
        if c.right!=None:
            s.push(c.right)
        if c.left!=None:
            s.push(c.left)

def iterativeee(root):
    s=stack()
    cur=root
    while cur!=None or s.empty()==False:
        while cur!=None:
            print(cur.key,end=" ")
            if cur.right!=None:
                s.push(cur.right)
            cur=cur.left
        if s.empty()==False:
            cur=s.pop()
            

root=Node(10)
n1=Node(20)
n2=Node(30)
n3=Node(40)
n4=Node(50)
root.left=n1
root.right=n2
n2.left=n3
n2.right=n4
preorder(root)
print()
iterative(root)
print()
iterativee(root)
print()
iterativeee(root)