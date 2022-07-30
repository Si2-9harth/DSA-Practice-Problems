class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

first=None
second=None
prev=None

def swap(root):
    global first, second, prev
    if root==None:
        return
    else:
        swap(root.left)
        if prev!=None and prev.key>=root.key:
            if first==None:
                first=prev 
            else:
                second=root
        prev=root   
        swap(root.right)

root=Node(18)
n1=Node(60)
n2=Node(4)
n3=Node(70)
n4=Node(8)
n5=Node(80)
root.left=n1
root.right=n3
n1.left=n2
n3.left=n4
n3.right=n5
swap(root)
print(first.key)
print(second.key)
first.key,second.key = second.key,first.key