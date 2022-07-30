class Node:
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None

def property(root):
    if root==None:
        return True
    elif root.left==None and root.right==None:
        return True
    else:
        sum=0
        if root.left!=None:
            sum+=root.left.key
        if root.right!=None:
            sum+=root.right.key
        return root.key==sum and property(root.left) and property(root.right)


root=Node(20)
n1=Node(8)
n2=Node(2)
n3=Node(5)
n4=Node(12)
root.left=n1
root.right=n4
n1.left=n2
n1.right=n3
print(property(root))