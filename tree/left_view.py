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

mxlevel=0
def left(root,level):
    if root==None:
        return
    else:
        global mxlevel
        if mxlevel<level:
            print(root.key,end=" ")
            mxlevel=level
        left(root.left,level+1)
        left(root.right,level+1)


def leftview(root):
    left(root,1)

def leftvieww(root):
    if root==None:
        return
    else:
        q=queue()
        q.push(root)
        while q.empty()==False:
            count=q.size()
            for i in range(count):
                c=q.pop()
                if i==0:
                    print(c.key,end=" ")
                if c.left!=None:
                    q.push(c.left)
                if c.right!=None:
                    q.push(c.right)

root=Node(20)
n1=Node(8)
n2=Node(3)
n3=Node(5)
n4=Node(12)
root.left=n1
root.right=n4
n1.left=n2
n1.right=n3
leftview(root)
print()
leftvieww(root)