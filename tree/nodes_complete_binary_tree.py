class Node:
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None

def count_nodes(root):
    if root==None:
        return 0
    else:
        return 1+count_nodes(root.left)+count_nodes(root.right)

def count_nodess(root):
    if root==None:
        return 0
    else:
        lh=0
        rh=0
        cur=root
        while cur!=None:
            cur=cur.left
            lh+=1

        cur=root
        while cur!=None:
            cur=cur.right
            rh+=1
        if lh==rh:
            return (2**lh)-1
        else:
            return 1+count_nodess(root.left)+count_nodess(root.right)

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
n4.left=n9
n4.right=n10
print(count_nodes(root))
print(count_nodess(root))
