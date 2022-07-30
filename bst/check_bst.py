class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def check1(root,min,max):
    if root==None:
        return True
    else:
        return (root.key>min and root.key<max) and check1(root.left,min,root.key) and check1(root.right,root.key,max)


prev=float('-inf')
def check2(root):
    if root==None:
        return True
    else:
        global prev
        if check2(root.left)==False:
            return False
        if root.key<=prev:
            return False
        prev=root.key
        return check2(root.right)


root=Node(80)
n1=Node(70)
n2=Node(60)
n3=Node(75)
n4=Node(90)
n5=Node(85)
n6=Node(100)
root.left=n1
root.right=n4
n1.left=n2
n1.right=n3
n4.left=n5
n4.right=n6
print(check1(root,float("-inf"),float("inf")))
print(check2(root))