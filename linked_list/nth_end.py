class Node:
    def __init__(self,val):
        self.val = val
        self.next=None
def printl(head):
    while head!=None:
        print(head.val,end="-->")
        head=head.next
    print("NULL")

def insert_begin(head,val):
    x=Node(val)
    x.next=head
    return x

def middle(head):
    if head==None:
        return
    else:
        count=0
        t=head
        while t!=None:
            t=t.next
            count+=1
        cur=head
        for i in range(0,count//2):
            cur=cur.next
        return cur.val

def end(head,n):
    if head==None:
        return
    else:
        l=0
        cur=head
        while cur!=None:
            cur=cur.next
            l+=1       
            pass
        if l<n:
            return
        else:
            cur=head
            i=0
            while i<l-n:
                i=i+1
                cur=cur.next
            return cur.val

def endd(head,n):
    if head==None:
        return
    else:
        f=head
        s=head
        for i in range(n):
            if f==None:
                return
            f=f.next

        while f!=None:
            f=f.next
            s=s.next
        return s.val   

head=Node(50)
head=insert_begin(head,40)
head=insert_begin(head,30)
head=insert_begin(head,20)
head=insert_begin(head,10)
head=insert_begin(head,5)
printl(head)
print(end(head,2))
print(endd(head,3))