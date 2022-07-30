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

def insert_end(head,val):
    if head==None:
        t=Node(val=val)
        return t
    else:
        cur=head
        while cur.next!=None:
            cur=cur.next
        t=Node(val=val)
        cur.next=t
        t.prev=cur
        return head

head=Node(10)
n2=Node(20)
n3=Node(30)
n2.prev=head
head.next=n2
n3.prev=n2
n2.next=n3
printl(head)
head=insert_end(head,40)
printl(head)