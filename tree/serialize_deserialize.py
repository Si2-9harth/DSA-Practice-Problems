class Node:
    def __init__(self,val):
        self.val = val
        self.left=None
        self.right=None

def serialize(root,a):
    if root==None:
        a.append(-1)
    else:
        a.append(root.val)
        serialize(root.left,a)
        serialize(root.right,a)

index=0

def deserialize(a):
    global index
    if index==len(a):
        return None
    else:
        v=a[index]
        index+=1
        if v==-1:
            return None
        else:
            root=Node(v)
            root.left=deserialize(a)
            root.right=deserialize(a)
            return root

def inorder(root):
    if root==None:
        return
    else:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)

root=Node(10)
n1=Node(20)
n2=Node(30)
n3=Node(40)
n4=Node(50)
root.left=n1
root.right=n2
n2.left=n3
n2.right=n4
a=[]
serialize(root,a)
print(a)
root=deserialize(a)
inorder(root)