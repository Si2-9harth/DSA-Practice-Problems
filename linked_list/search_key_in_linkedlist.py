class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

def insert_begin(head,val):
    t=Node(val)
    if head==None:
        return t  
    else:
        t.next=head
        return t

def printl(head):
    while head!=None:
        print(head.val,end="--->")
        head=head.next
    print("NULL")

def search(head,val):
    i=1
    cur=head
    while cur!=None:
        if cur.val==val:
            return i   
        else:
            cur=cur.next
            i=i+1
    return -1

def searchr(head,val):
    if head==None:
        return -1
    elif head.val==val:
        return 1
    else:
        res=searchr(head.next,val)
        if res==-1:
            return -1
        else:
            return 1+res

head=Node(60)
head=insert_begin(head,50)
head=insert_begin(head,40)
head=insert_begin(head,30)
head=insert_begin(head,20)
head=insert_begin(head,10)
printl(head)
print(search(head,40))
print(search(head,45))
print(searchr(head,40))
print(searchr(head,45))
