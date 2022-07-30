class Node:
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None

def inorder(root):
    if root==None:
        return
    else:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)

def getsuccessor(root):
    c=root.right
    while c!=None and c.left!=None:
        c=c.left
    return c

def delete(root,k):
    if root==None:
        return None
    if root.key>k:
        root.left=delete(root.left,k)
    elif root.key<k:
        root.right=delete(root.right,k)
    else:
        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            cur=getsuccessor(root)
            root.key=cur.key
            root.right=delete(root.right,cur.key)
    return root
    


root=Node(50)
n1=Node(30)
n2=Node(70)
n3=Node(40)
n4=Node(60)
n5=Node(80)
root.left=n1
root.right=n2
n1.right=n3
n2.left=n4
n2.right=n5
inorder(root)
root=delete(root,50)
print()
inorder(root)