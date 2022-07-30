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

def reverse_r(head,k):
    p=None
    cur=head
    next=None
    count=0
    while cur!=None and count<k:
        n=cur.next
        cur.next=p
        p=cur
        cur=n
        count+=1
    if n!=None:
        res=reverse_r(n,k)
        head.next=res
    return p   

def reverse_i(head,k):
    cur=head
    pf=None
    isfp=True
    while cur!=None:
        f=cur
        count=0
        p=None
        while cur!=None and count<k:
            n=cur.next
            cur.next=p
            p=cur
            cur=n
            count+=1
        if isfp:
            head=p
            isfp=False
        else:
            pf.next=p
        pf=f   
    return head     

head=Node(7)
head=insert_begin(head,6)
head=insert_begin(head,5)
head=insert_begin(head,4)
head=insert_begin(head,3)
head=insert_begin(head,2)
head=insert_begin(head,1)
printl(head)
head=reverse_r(head,3)
printl(head)
head=reverse_i(head,3)
printl(head)

