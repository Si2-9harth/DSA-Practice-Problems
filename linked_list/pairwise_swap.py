from sympy import N


class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def printl(head):
    while head!=None:
        print(head.val,end="-->")
        head=head.next
    print("NULL")

def swap(h1):
    cur=h1
    while cur!=None and cur.next!=None:
        n=cur.next
        cur.val,n.val=n.val,cur.val
        cur=n.next

def swape(head):
    if head==None or head.next==None:
        return head
    else:
        cur=head
        n=cur.next.next
        cur.next.next=cur
        p=cur
        cur=n 
        head=head.next
        while cur!=None and cur.next!=None:
            p.next=cur.next
            n=cur.next.next
            cur.next.next=cur
            p=cur
            cur=n
        p.next=cur
        return head

h1=Node(1)
n1=Node(2)
n2=Node(3)
n3=Node(4)
n4=Node(5)
h1.next=n1
n1.next=n2
n2.next=n3
n3.next=n4
printl(h1)
swap(h1)
printl(h1)
head=swape(h1)
printl(head)
