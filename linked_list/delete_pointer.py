class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def delete(node):
    nextt=node.next
    node.val=nextt.val
    node.next=nextt.next
    nextt=None

    

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
printl(head)
delete(n2)
printl(head)

