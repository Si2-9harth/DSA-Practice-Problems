class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def printlst(head):
    while head!=None:
        print(head.val,end=" ---> ")
        head=head.next
    print("NULL")

def recursive_p(head):
    if head==None:
        print("NULL")
        return
    else:
        print(head.val,end=" ---> ")
        return recursive_p(head.next)


head=Node(1)
n1=Node(2)
n2=Node(3)
n3=Node(4)
head.next=n1
n1.next=n2
n2.next=n3
printlst(head)
recursive_p(head)