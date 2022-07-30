class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class pair:
    def __init__(self,node,hd):
        self.node=node
        self.hd=hd

class queue:
    def __init__(self):
        self.arr=[]
    def empty(self):
        return self.arr==[]
    def push(self,val):
        self.arr.append(val)
    def pop(self):
        return self.arr.pop(0)
    def size(self):
        return len(self.arr)

def vertical(root):
    if root==None:
        return     
    else:
        q=queue()
        map=dict()
        q.push(pair(root,0))
        while q.empty()==False:
            c=q.pop()
            hd=c.hd
            cur=c.node
            if hd not in map.keys():
                map[hd]=cur.key 
            if cur.left!=None:
                q.push(pair(cur.left,hd-1))
            if cur.right!=None:
                q.push(pair(cur.right,hd+1))
        for i in sorted(map.keys()):
            print(map[i],end=" ")


root=Node(10)
n1=Node(20)
n2=Node(30)
n3=Node(5)
n4=Node(15)
root.left=n1
root.right=n2
n1.left=n3
n1.right=n4
vertical(root)