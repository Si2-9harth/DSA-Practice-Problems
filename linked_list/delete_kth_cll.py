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

def delete_k(head,k):
    if head==None:
        return head
    elif k==1:
        if head.next==head:
            head=None
            return head
        else:
            head.next.val,head.val=head.val,head.next.val
            t=head.next
            head.next=head.next.next
            t=None
            return head
    else:
        i=1
        cur=head
        while i<k-1:
            cur=cur.next
            i=i+1
        t=cur.next
        cur.next=t.next
        t=None
        return head



head=insert_begin(None,80)
head=insert_begin(head,70)
head=insert_begin(head,60)
head=insert_begin(head,50)
head=insert_begin(head,40)
head=insert_begin(head,30)
head=insert_begin(head,20)
head=insert_begin(head,10)
printl(head)
head=delete_k(head,10)
printl(head)
head=delete_k(head,2)
printl(head)
head=delete_k(head,6)
printl(head)
