class Node:
    def __init__(self,val):
        self.val = val
        self.next=None
def printl(head):
    while head!=None:
        print(head.val,end="-->")
        head=head.next
    print("NULL")

def insert_begin(head,val):
    x=Node(val)
    x.next=head
    return x

def remove(head):
    cur=head
    while cur!=None and cur.next!=None:
        n=cur.next
        if n.val==cur.val:
            cur.next=n.next
            n=None
        else:
            cur=cur.next
    return head

head=Node(50)
head=insert_begin(head,50)
head=insert_begin(head,30)
head=insert_begin(head,20)
head=insert_begin(head,20)
head=insert_begin(head,20)
head=insert_begin(head,10)
printl(head)
head=remove(head)
printl(head)
