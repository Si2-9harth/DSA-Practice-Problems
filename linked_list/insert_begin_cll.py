class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=next

def printl(head):
    if head!=None:
        print(head.val,end="-->")
        t=head.next
        while t!=head:
            print(t.val,end="-->")
            t=t.next
        print("NULL")

def insert_begin(head,val):
    x=Node(val)
    if head==None:
        x.next=x
        return x
    else:
        x.next=head
        t=head
        while t.next!=head:
            t=t.next
        t.next=x
        return x

head=insert_begin(None,10)
head=insert_begin(head,20)
head=insert_begin(head,30)
head=insert_begin(head,40)
printl(head)