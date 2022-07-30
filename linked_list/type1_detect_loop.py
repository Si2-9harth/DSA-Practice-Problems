class Node:
    def __init__(self,val=None):
        self.vis=0
        self.val=val
        self.next=None

def detect(head):
    cur=head
    while cur!=None:
        if cur.vis==1:
            return True
        else:
            cur.vis=1
            cur=cur.next
    return False

head=Node(15)
n1=Node(10)
n2=Node(12)
n3=Node(20)
head.next=n1
n1.next=n2
n2.next=n3
n3.next=n1
print(detect(head))