class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None
        self.prev=None

def printl(head):
    t=head
    print(t.val,end="-->")
    t=t.next
    while t!=head:
        print(t.val,end="-->")
        t=t.next
    print("NULL")

def insert_begin(head,val):
    x=Node(val)
    if head==None:
        x.next=x
        x.prev=x
        return x
    else:
        x.next=head
        x.prev=head.prev
        head.prev.next=x
        head.prev=x
        return x

def insert_end(head,val):
    x=Node(val)
    if head==None:
        x.next=x
        x.prev=x
        return x
    else:
        x.next=head
        x.prev=head.prev
        head.prev.next=x
        head.prev=x
        return head


head=Node(10)
n1=Node(20)
n2=Node(30)
n3=Node(40)
n4=Node(50)
head.next=n1
head.prev=n4
n1.next=n2
n1.prev=head
n2.next=n3
n2.prev=n1
n3.next=n4
n3.prev=n2
n4.next=head
n4.prev=n3
printl(head)
head=insert_begin(head,5)
printl(head)
head=insert_end(head,60)
printl(head)