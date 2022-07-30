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

def ceiling(root,k):
    if root==None:
        return -1
    else:
        res=-1
        cur=root
        while cur!=None:
            if cur.key==k:
                return k
            else:
                if cur.key>k:
                    res=cur.key
                    cur=cur.left
                else:
                    cur=cur.right
        return res
                    
    

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
print()
print(ceiling(root,48))
