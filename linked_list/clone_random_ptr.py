class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None
        self.random=None

def print_r(head):
    while head!=None:
        print(f"Node {head.val} has random at Node {head.random.val}")
        head=head.next
    print()

def hashing(head):
    hm=dict()
    cur=head
    while cur!=None:
        if cur not in hm.keys():
            hm[cur]=Node(cur.val)
        cur=cur.next
    
    

head=Node(10)
n1=Node(5)
n2=Node(20)
n3=Node(15)
n4=Node(20)
head.next=n1
n1.next=n2
n2.next=n3
n3.next=n4
head.random=n2
n1.random=n3
n2.random=head
n3.random=n2
n4.random=n3
print_r(head)
h2=hashing(head)
print_r(h2)