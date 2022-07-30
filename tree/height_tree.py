class Node:
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None

def height(root):
    if root==None:
        return 0
    else:
        return max(height(root.left),height(root.right))+1
    

root=Node(10)
n1=Node(20)
n2=Node(30)
n3=Node(40)
n4=Node(50)
root.left=n1
root.right=n2
n2.left=n3
n2.right=n4
print(height(root))