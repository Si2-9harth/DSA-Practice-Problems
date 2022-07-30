class Node:
    def __init__(self,key=None):
        self.key = key
        self.left=None
        self.right=None

class queue:
    def __init__(self):
        self.arr=[]
    def empty(self):
        return self.arr==[]
    def size(self):
        return len(self.arr)
    def push(self,value):
        self.arr.append(value)
    def pop(self):
        if self.empty():
            return
        else:
            return self.arr.pop(0)

class stack:
    def __init__(self):
        self.arr=[]
    def empty(self):
        return self.arr==[]
    def size(self):
        return len(self.arr)
    def push(self,value):
        self.arr.append(value)
    def pop(self):
        if self.empty():
            return
        else:
            return self.arr.pop()


def spiral1(root):
    if root==None:
        return
    else:
        q=queue()
        s=stack()
        reverse=False
        q.push(root)
        while q.empty()==False:
            count=q.size()
            for i in range(count):
                c=q.pop()
                if reverse:
                    s.push(c)
                if not reverse:
                    print(c.key,end=' ')
                if c.left!=None:
                    q.push(c.left)
                if c.right!=None:
                    q.push(c.right)
            if reverse:
                while s.empty()==False:
                    print(s.pop().key,end=" ")
            reverse=not reverse


def spiral2(root):
    if root==None:
        return 
    else:
        s1=stack()
        s2=stack()
        s1.push(root)
        while s1.empty()==False or s2.empty()==False:
            while s1.empty()==False:
                c=s1.pop()
                print(c.key,end=" ")
                if c.left!=None:
                    s2.push(c.left)
                if c.right!=None:
                    s2.push(c.right)
            while s2.empty()==False:
                c=s2.pop()
                print(c.key,end=" ")
                if c.right!=None:
                    s1.push(c.right)
                if c.left!=None:
                    s1.push(c.left)
                


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
spiral1(root)
print()
spiral2(root)