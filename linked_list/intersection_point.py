class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def printl(head):
    while head!=None:
        print(head.val,end="-->")
        head=head.next
    print("NULL")

def intersection(h1,h2):
    s=set()
    cur=h1
    while cur!=None:
        s.add(cur)
        cur=cur.next
    cur=h2
    while cur!=None:
        if cur in s:
            return cur.val
        cur=cur.next
    return

def intersection_e(h1,h2):
    c1=0
    c2=0
    cur=h1
    while cur!=None:
        c1+=1
        cur=cur.next
    cur=h2
    while cur!=None:
        c2+=1
        cur=cur.next
    if c1>c2:
        cur1=h1
        cur2=h2
        d=abs(c2-c1)
        i=0
        while cur1!=None and i<d:
            cur1=cur1.next
            i+=1
        while cur1!=None and cur2!=None:
            if cur1==cur2:
                return cur1.val
            cur1=cur1.next
            cur2=cur2.next
    else:
        cur1=h1
        cur2=h2
        d=abs(c2-c1)
        i=0
        while cur2!=None and i<d:
            cur2=cur2.next
            i+=1
        while cur1!=None and cur2!=None:
            if cur1==cur2:
                return cur1.val
            cur1=cur1.next
            cur2=cur2.next
    return

h1=Node(5)
n1=Node(8)
n2=Node(7)
n3=Node(10)
n4=Node(12)
n5=Node(15)
h2=Node(9)
h1.next=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
h2.next=n3
printl(h1)
printl(h2)
print(intersection(h1,h2))
print(intersection_e(h1,h2))