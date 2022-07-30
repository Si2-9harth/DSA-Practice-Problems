class Node:
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None

def postorder(root):
    if root!=None:
        postorder(root.left)
        postorder(root.right)
        print(root.key,end=" ")

root=Node(10)
n1=Node(20)
n2=Node(30)
n3=Node(40)
n4=Node(50)
root.left=n1
root.right=n2
n2.left=n3
n2.right=n4
postorder(root)