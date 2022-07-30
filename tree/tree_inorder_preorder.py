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

def preorder(root):
    if root==None:
        return
    else:
        print(root.key,end=" ")
        preorder(root.left)
        preorder(root.right)
        
preindex=0

def create(ia,pa,start,end):
    if start>end:
        return None
    else:
        global preindex
        root=Node(pa[preindex])
        preindex+=1
        index=ia.index(root.key)

        root.left=create(ia,pa,start,index-1)
        root.right=create(ia,pa,index+1,end)
        return root




ia=[20,10,40,30,50]
pa=[10,20,30,40,50]
root=create(ia,pa,0,len(ia)-1)
inorder(root)
print()
preorder(root)