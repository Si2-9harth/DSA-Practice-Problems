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

def d(root):
    if root==None:
        return 0
    else:
        d1=1+height(root.left)+height(root.right)
        d2=d(root.left)
        d3=d(root.right)
        return max(d1,max(d2,d3))         
res=0
def dia(root):
    if root==None:
        return 0
    else:
        global res
        lh=dia(root.left)
        rh=dia(root.right)
        res=max(res,1+lh+rh)
        return 1+max(lh,rh)



root=Node(1)
n1=Node(2)
n2=Node(3)
n3=Node(4)
n4=Node(5)
n5=Node(6)
n6=Node(7)
n7=Node(8)
n8=Node(9)
n9=Node(10)
n10=Node(11)
root.left=n1
root.right=n2
n1.left=n3
n1.right=n4
n2.left=n5
n2.right=n6
n3.left=n7
n3.right=n8
n5.left=n9
n5.right=n10
print(d(root))
dia(root)
print(res)