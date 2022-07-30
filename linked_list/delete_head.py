class Node:
    def __init__(self,val=None):
        self.val = val
        self.next=None

def insert_begin(head,val):
    temp=Node(val)
    if not head:
        return temp
    else:
        temp.next=head
        return temp

def printl(head):
    while head.next!=None:
        print(head.val,end="--->")
        head=head.next
    print(head.val)
def delete_begin(head):
    if not head:
        return None
    else:
        temp=head
        head=head.next
        temp=None
        return head

head=Node()
head=insert_begin(head,30)
head=insert_begin(head,20)
head=insert_begin(head,10)
printl(head)
head=delete_begin(head)
printl(head)