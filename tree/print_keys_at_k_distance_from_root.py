from sympy import N


class Node:
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None

def kdist(root,k):
    if root==None:
        return
    elif k==0:
        print(root.key,end=' ')
    else:
        kdist(root.left,k-1)
        kdist(root.right,k-1)
    

root=Node(10)
n1=Node(20)
n2=Node(30)
n3=Node(40)
n4=Node(50)
n5=Node(70)
n6=Node(80)
root.left=n1
root.right=n2
n1.left=n3
n1.right=n4
n2.right=n5
n5.right=n6
kdist(root,2)