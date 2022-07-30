class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class stack:
    def __init__(self):
        self.head=None
        self.l=0
    
    def is_empty(self):
        if self.l==0:
            return True
        else:
            return False
    
    def push(self,val):
        x=Node(val)
        if self.head==None:
            self.head=x
            self.l+=1
        else:
            x.next=self.head
            self.head=x
            self.l+=1

    def pop(self):
        if self.head==None:
            return "ERROR STACK IS EMPTY"
        else:
            res=self.head.val
            self.head=self.head.next
            self.l-=1
            return res 

    def peek(self):
        return self.head.val

    def size(self):
        return self.l



s=stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())
print(s.pop())
print(s.size())
s.push(40)
print(s.peek())
print(s.is_empty())