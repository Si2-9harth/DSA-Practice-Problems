class Node:
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None
class dist:
    def __init__(self,val=-1):
        self.val=val
res=0
def btime(root,leaf,d):
    global res
    if root==None:
        return 0
    if root.key==leaf:
        d.val=0
        return 1
    ldist=dist()
    rdist=dist()
    lh=btime(root.left,leaf,ldist)
    rh=btime(root.right,leaf,rdist)
    if ldist.val!=-1:
        d.val=ldist.val+1
        res=max(res,rh+d.val)
    elif rdist.val!=-1:
        d.val=rdist.val+1
        res=max(res,lh+d.val)
    return max(lh,rh)+1

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
d=dist()
print(btime(root,8,d))
print(res)
