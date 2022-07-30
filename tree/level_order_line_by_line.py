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

def levelorder(root):
    if root==None:
        return
    else:
        q=queue()
        q.push(root)
        q.push(None)
        while q.size()>1:
            c=q.pop()
            if c==None:
                q.push(None)
                print()
            else:
                print(c.key,end=" ")
                if c.left!=None:
                    q.push(c.left)
                if c.right!=None:
                    q.push(c.right)

def level(root):
    if root==None:
        return
    else:
        q=queue()
        q.push(root)
        while q.empty()==False:
            count=q.size()
            for i in range(count):
                c=q.pop()
                print(c.key,end=" ")
                if c.left!=None:
                    q.push(c.left)
                if c.right!=None:
                    q.push(c.right)
            print()


root=Node(10)
n1=Node(15)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
n6=Node(60)
n7=Node(70)
root.left=n1
root.right=n2
n1.left=n3
n2.left=n4
n2.right=n5
n4.left=n6
n4.right=n7

levelorder(root)
print()
level(root)