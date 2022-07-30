class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

def printl(head):
    while head!=None:
        print(head.val,end="--->")
        head=head.next
    print()
def insert_end(head,val):
    temp=Node(val)
    if head==None:
        return temp
    else:
        cur=head
        while cur.next!=None:
            cur=cur.next
        cur.next=temp
        return head

def delete_tail(head):
    if head==None:
        return None
    elif head.next==None:
        temp=head
        head=None
        temp=None
        return head
    else:
        cur=head
        while cur.next.next!=None:
            cur=cur.next
        temp=cur.next
        cur.next=None
        temp=None
        return head


head=Node()
head=insert_end(head,10)
head=insert_end(head,20)
head=insert_end(head,30)
printl(head)
head=delete_tail(head)
printl(head)