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
    q=queue()
    q.push(pair(root,0))
    map=dict()
    while q.empty()==False:
        c=q.pop()
        hd=c.hd
        if c.hd in map.keys():
            map[hd].append(c.node.key)
        else:
            map[hd]=[c.node.key]
        if c.node.left!=None:
            q.push(pair(c.node.left,c.hd-1))
        if c.node.right!=None:
            q.push(pair(c.node.right,c.hd+1))

    for i in sorted(map.keys()):
        for j in map[i]:
            print(j,end=" ")
        print()

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