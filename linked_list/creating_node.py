class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

n1=Node(1)
n2=Node(2)
n3=Node(3)
n1.next=n2
n2.next=n3
print(n1.next)