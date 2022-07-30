class Node:
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None

def height(root):
    if root==None:
        return 0
    else:
        return max(height(root.left), height(root.right))+1

def check(root):
    if root==None:
        return True
    lh=height(root.left)
    rh=height(root.right)
    return abs(lh-rh)<=1 and check(root.left) and check(root.right)

def chekk(root):
    if root==None:
        return 0
    lh=chekk(root.left)
    if lh==-1:
        return -1
    rh=chekk(root.right)
    if rh==-1:
        return -1
    if abs(rh-lh)>1:
        return -1
    else:
        return max(lh,rh)+1

root=Node(20)
n1=Node(8)
n2=Node(2)
n3=Node(5)
n4=Node(12)
n5=Node(7)
root.left=n1
root.right=n4
n1.left=n2
n2.left=n5
n4.right=n3
print(check(root))
print(chekk(root))