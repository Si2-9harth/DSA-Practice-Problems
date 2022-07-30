class Node:
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None

def recursive(root,k):
    x=Node(k)
    if root==None:
        return x
    else:
        if root.key>k:
            root.left=recursive(root.left,k)
        else:
            root.right=recursive(root.right,k)
        return root

def iterative(root,k):
    t=Node(k)
    parent=None
    cur=root
    while cur!=None:
        parent=cur
        if cur.key>k:
            cur=cur.left
        elif cur.key<k:
            cur=cur.right
        else:
            return root
    if parent==None:
        return t 
    elif parent.key>k:
        parent.left=t 
    else:
        parent.right=t
    return root

def inorder(root):
    if root==None:
        return
    else:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)

root=Node(10)
n1=Node(8)
n2=Node(30)
n3=Node(25)
n4=Node(50)
root.left=n1
root.right=n2
n2.left=n3
n2.right=n4
root=recursive(root,31)
inorder(root)
root=iterative(root,9)
print()
inorder(root)