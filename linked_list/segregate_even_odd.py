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

def segregate(head):
    estart=None
    estop=None
    ostart=None
    ostop=None
    cur=head
    while cur!=None:
        if cur.val%2==0:
            if estart==None:
                estart=cur
                estop=cur
            else:
                estop.next=cur
                estop=estop.next
        else:
            if ostart==None:
                ostart=cur
                ostop=cur
            else:
                ostop.next=cur
                ostop=ostop.next
        cur=cur.next
    if ostop==None or estop==None:
        return head
    estop.next=ostart
    ostop.next=None
    return estart

head=Node()
head=insert_end(head,17)
head=insert_end(head,15)
head=insert_end(head,8)
head=insert_end(head,12)
head=insert_end(head,10)
head=insert_end(head,5)
head=insert_end(head,4)
printl(head)
head=segregate(head)
printl(head)