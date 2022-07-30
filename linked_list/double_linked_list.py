class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
        self.prev = None

n1=Node(10)
n2=Node(20)
n3=Node(30)
n2.prev=n1
n1.next=n2
n3.prev=n2
n2.next=n3
