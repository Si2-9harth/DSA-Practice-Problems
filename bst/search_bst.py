class Node:
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None

def recursive(root,k):
    if root==None:
        return False
    elif root.key==k:
        return True
    else:
        if root.key>k:
            return recursive(root.left,k)
        else:
            return recursive(root.right,k)

def iterative(root,k):
    if root==None:
        return False
    else:
        cur=root
        while cur!=None:
            if cur.key==k:
                return True
            if cur.key<k:
                cur=cur.right
            else:
                cur=cur.left
        return False

root=Node(10)
n1=Node(8)
n2=Node(30)
n3=Node(25)
n4=Node(50)
root.left=n1
root.right=n2
n2.left=n3
n2.right=n4
print(recursive(root,50))
print(iterative(root,49))