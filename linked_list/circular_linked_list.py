class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

head=Node(10)
n2=Node(20)
n3=Node(30)
head.next=n2
n2.next=n3
n3.next=head