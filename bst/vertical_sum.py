from tkinter import NO


class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def vertical_s(root,hd,map):
    if root==None:
        return
    else:
        vertical_s(root.left,hd-1,map)
        if hd not in map.keys():
            map[hd] = root.key
        else:
            map[hd]+=root.key
        vertical_s(root.right,hd+1,map)

def vertical(root):
    map=dict()
    vertical_s(root,0,map)
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