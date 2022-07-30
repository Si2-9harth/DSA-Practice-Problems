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

def insert_end(head,val):
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
        return head

def insert_endd(head,val):
    t=Node(val)
    if head==None:
        t.next=t
        return t
    else:
        t.next=head.next
        head.next=t
        t.val,head.val=head.val,t.val
        return t


head=insert_end(None,10)
head=insert_end(head,20)
head=insert_end(head,30)
head=insert_end(head,40)
printl(head)
head=insert_endd(head,50)
head=insert_endd(head,60)
head=insert_endd(head,70)
printl(head)