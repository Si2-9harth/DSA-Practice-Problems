class Node:
    def __init__(self,val=None):
        self.val = val
        self.next=None

def printl(head):
    while head.next!=None:
        print(head.val,end="-->")
        head=head.next
    print(head.val)

def insert_begin(head,val):
    x=Node(val)
    x.next=head
    return x

head=Node()
head=insert_begin(head,30)
head=insert_begin(head,20)
head=insert_begin(head,10)
printl(head)


