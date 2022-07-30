class Node:
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None

def path(root,n,p):
    if root==None:
        return False
    p.append(root.key)
    if root.key==n:
        return True
    if path(root.left,n,p) or path(root.right,n,p):
        return True
    p.pop()
    return False

def lca1(root,n1,n2):
    if root==None:
        return
    else:
        p1=[]
        p2=[]
        if path(root,n1,p1)==False or path(root,n2,p2)==False:
            return
        else:
            i=0
            while i<len(p1)-1 and i<len(p2)-1:
                if p1[i+1]!=p2[i+1]:
                    return p1[i] 
                i+=1

def lca2(root,n1,n2):
    if root==None:
        return
    if root.key==n1 or root.key==n2:
        return root.key
    lc1=lca2(root.left,n1,n2)
    lc2=lca2(root.right,n1,n2)
    if lc1!=None and lc2!=None:
        return root.key
    if lc2==None:
        return lc1
    else:
        return lc2

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
print(lca1(root,9,5))
print(lca2(root,9,5))
