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
    if head==None:
        return
    else:
        cur=head
        p=None
        while cur!=None:
            n=cur.next
            cur.next=p
            p=cur
            cur=n
        return p

head=Node(50)
head=insert_begin(head,40)
head=insert_begin(head,30)
head=insert_begin(head,20)
head=insert_begin(head,10)
head=insert_begin(head,5)
printl(head)
head=reverse(head)
printl(head)