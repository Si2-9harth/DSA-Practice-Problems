class Node:
    def __init__(self,val=None):
        self.val = val
        self.next=None

def printl(head):
    while head!=None:
        print(head.val,end="-->")
        head=head.next
    print("NULL")

def insert_end(head,val):
    t=Node(val)
    if head==None:
        return t
    else:
        cur=head
        while cur.next!=None:
            cur=cur.next
        cur.next=t
        return head

def insert_pos(head,pos,val):
    if pos==1:
        t=Node(val)
        t.next=head
        return t
    else:
        cur=head
        i=1
        while i<=pos-2 and cur!=None:
            cur=cur.next
            i=i+1
        if cur==None:
            return head

        t=Node(val)
        t.next=cur.next
        cur.next=t
        return head


head=Node(10)
head=insert_end(head,20)
head=insert_end(head,30)
head=insert_end(head,40)
head=insert_end(head,50)
head=insert_end(head,60)
printl(head)
head=insert_pos(head,4,45)
printl(head)
