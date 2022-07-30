class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
        self.prev = None

def printl(head):
    while head!=None:
        print(head.val,end="--->")
        head=head.next
    print("NULL")

def insert_begin(head,val):
    t=Node(val)
    if head==None:
        return t
    else:
        head.prev=t
        t.next=head
        return t

head=Node(10)
n2=Node(20)
n3=Node(30)
n2.prev=head
head.next=n2
n3.prev=n2
n2.next=n3
printl(head)
head=insert_begin(head,5)
printl(head)
