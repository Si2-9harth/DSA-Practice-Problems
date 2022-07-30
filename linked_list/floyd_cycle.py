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
            return True
    return False   

head=Node(15)
n1=Node(10)
n2=Node(12)
n3=Node(20)
head.next=n1
n1.next=n2
n2.next=n3
#n3.next=n1
print(detect(head))