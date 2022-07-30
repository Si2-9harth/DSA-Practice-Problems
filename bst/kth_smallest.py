class Node:
    def __init__(self,val=None):
        self.val=val
        self.left=None
        self.right=None
        self.lcount=0
    
def insert(root,val):
    if root==None:
        return Node(val)
    else:
        if root.val>val:
            root.lcount+=1
            root.left=insert(root.left,val)
        else:
            root.right=insert(root.right,val)
    return root  

def get_successor(root):
    c=root
    c=c.right
    while c!=None and c.left!=None:
        c=c.left
    return c

def delete(root,val):
    if root==None:
        return None
    else:
        if val>root.val:
            root.right=delete(root.right,val)
        elif val<root.val:
            root.left=delete(root.left,val)
            root.lcount-=1
        else:
            if root.right==None:
                return root.left  
            elif root.left==None:
                return root.right
            else:
                c=get_successor(root)
                root.key=c.key
                root.right=delete(root.right,c.val)

def kth(root,k):
    if root==None:
        return -1
    else:
        if root.lcount+1==k:
            return root.val
        elif root.lcount+1>k:
            return kth(root.left,k)
        else:
            return kth(root.right,k-root.lcount-1)

def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)


keys=[20, 8, 22, 4, 12, 10, 14]
root=None
for i in keys:
    root=insert(root,i)
root=insert(root,17)
k=4
inorder(root)
print()
print(kth(root,7))