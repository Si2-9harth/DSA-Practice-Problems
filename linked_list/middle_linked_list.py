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

def middle(head):
    if head==None:
        return
    else:
        count=0
        t=head
        while t!=None:
            t=t.next
            count+=1
        cur=head
        for i in range(0,count//2):
            cur=cur.next
        return cur.val

def middlee(head):
    if head==None:
        return 
    else:
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
        return slow.val

head=Node(50)
head=insert_begin(head,40)
head=insert_begin(head,30)
head=insert_begin(head,20)
head=insert_begin(head,10)
#head=insert_begin(head,5)
printl(head)
print(middle(head))
print(middlee(head))