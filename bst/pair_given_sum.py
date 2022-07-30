class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
s=set()
def check(root,sum):
    if root==None:
        return False
    else:
        global s
        if check(root.left,sum)==True:
            return True
        if sum-root.key in s:
            return True
        else:
            s.add(root.key)
        return check(root.right,sum)

root=Node(10)
n1=Node(5)
n2=Node(20)
n3=Node(16)
n4=Node(40)
root.left=n1
root.right=n2
n2.left=n3
n2.right=n4
print(check(root,20))