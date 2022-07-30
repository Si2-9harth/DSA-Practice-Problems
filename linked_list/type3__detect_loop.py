class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def detect(head):
    s=set()
    cur=head
    while cur!=None:
        if cur in s:
            return True
        else:
            s.add(cur)
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