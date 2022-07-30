class Node:
    def __init__(self,val=None):
        self.val = val
        self.next=None

def printl(head):
    while head.next!=None:
        print(head.val,end="-->")
        head=head.next
    print(head.val)

def insert_end(head,val):
    x=Node(val)
    if head.val==None:
        return x
    else:
        cur=head
        while cur.next!=None:
            cur=cur.next
        cur.next=x
        return head

head=Node()
head=insert_end(head,10)
head=insert_end(head,20)
head=insert_end(head,30)
printl(head)