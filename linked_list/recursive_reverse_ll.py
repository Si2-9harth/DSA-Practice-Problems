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

def reverse(head):
    if head==None or head.next==None:
        return head
    
    res_head=reverse(head.next)
    n=head.next
    n.next=head
    head.next=None
    return res_head

def reverser(cur,prev):
    if cur==None:
        return prev
    n=cur.next
    cur.next=prev
    prev=cur
    cur=n
    return reverser(cur,prev)

head=Node(50)
head=insert_begin(head,40)
head=insert_begin(head,30)
head=insert_begin(head,20)
head=insert_begin(head,10)
head=insert_begin(head,5)
printl(head)
head=reverse(head)
printl(head)
head=reverser(head,None)
printl(head)