class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
        self.prev = None

def printl(head):
    while head!=None:
        print(head.val,end="--->")
        head=head.next
    print("NULL")

def delete(head):
    if head==None:
        return None
    elif head.next==None:
        head=None
        return head
    else:
        t=head
        head=head.next
        head.prev=None
        t=None
        return head
        

head=Node(10)
n2=Node(20)
n3=Node(30)
n2.prev=head
head.next=n2
n3.prev=n2
n2.next=n3
printl(head)
head=delete(head)
printl(head)