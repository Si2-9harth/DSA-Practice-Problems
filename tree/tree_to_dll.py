class Node:
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None

def printl(head):
    while head!=None:
        print(head.key,end="-->")
        head=head.right
    print("NULL")
prev=None
def dll(root):
    global prev
    if root==None:
        return root
    head=dll(root.left)
    if prev==None:
        head=root
        prev=root
    else:
        root.left=prev
        prev.right=root
    prev=root
    dll(root.right)
    return head



root=Node(20)
n1=Node(8)
n2=Node(2)
n3=Node(5)
n4=Node(12)
n5=Node(0)
root.left=n1
root.right=n4
n1.left=n2
n1.right=n3
n4.left=n5
head=dll(root)
printl(head)