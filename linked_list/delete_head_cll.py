class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def printl(head):
    if head!=None:
        print(head.val,end="-->")
        t=head
        t=t.next
        while t!=head:
            print(t.val,end="-->")
            t=t.next
        print("NULL")

def delete_head(head):
    if head==None:
        return None
    elif head.next==head:
        head=None
        return head
    else:
        cur=head
        while cur.next!=head:
            cur=cur.next
        t=head
        cur.next=head.next
        head=cur.next
        t=None
        
        return head
def delete_headd(head):
    if head==None:
        return None
    elif head.next==head:
        head=None
        return head
    else:
        head.val,head.next.val=head.next.val,head.val
        t=head.next
        head.next=head.next.next
        t=None
        return head


head=Node(10)
n2=Node(20)
n3=Node(30)
head.next=n2
n2.next=n3
n3.next=head
printl(head)
head=delete_head(head)
printl(head)
head=delete_headd(head)
printl(head)