class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def detect(head):
    s=head
    f=head
    while f!=None and f.next!=None:
        s=s.next
        f=f.next.next
        if s==f:
            break
    if s!=f:
        return
    else:
        s=head
        while s.next!=f.next:
            s=s.next
            f=f.next
        f.next=None
     
def length_loop(head):
    s=head
    f=head
    while f!=None and f.next!=None:
        s=s.next
        f=f.next.next
        if s==f:
            break
    if s!=f:
        return
    else:
        c=1
        s=s.next
        while s!=f:
            s=s.next
            c+=1
        return c

def val_fn_loop(head):
    s=head
    f=head
    while f!=None and f.next!=None:
        s=s.next
        f=f.next.next
        if s==f:
            break
    if s!=f:
        return 0
    else:
        s=head
        while s!=f:
            s=s.next
            f=f.next
        return f.val

def printl(head):
    while head!=None:
        print(head.val,end="--->")
        head=head.next
    print("NULL")

head=Node(15)
n1=Node(10)
n2=Node(12)
n3=Node(20)
head.next=n1
n1.next=n2
n2.next=n3
n3.next=n1
print(val_fn_loop(head))
print(length_loop(head))
detect(head)
printl(head)

