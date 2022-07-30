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

def reverse(head):
    if head==None or head.next==None:
        return head
    else:
        cur=head
        while cur!=None:
            previous=cur.prev
            nex=cur.next
            cur.next=previous
            cur.prev=nex
            cur=cur.prev
        return previous.prev

head=Node(10)
n2=Node(20)
n3=Node(30)
n2.prev=head
head.next=n2
n3.prev=n2
n2.next=n3
printl(head)
head=reverse(head)
printl(head)