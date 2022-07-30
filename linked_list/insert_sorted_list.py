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

def insert(head,val):
    x=Node(val)
    if head==None:
        return x
    elif val<head.val:
        x.next=head
        return x
    else:
        cur=head
        while cur.next!=None and cur.next.val<=val:
            cur=cur.next
        x.next=cur.next
        cur.next=x
        return head


head=Node(50)
head=insert_begin(head,40)
head=insert_begin(head,30)
head=insert_begin(head,20)
head=insert_begin(head,10)
printl(head)
head=insert(head,5)
head=insert(head,35)
head=insert(head,55)
printl(head)

