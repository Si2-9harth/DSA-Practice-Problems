class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def empty(self):
        return self.front==None
    def getfront(self):
        return self.front
    def getrear(self):
        return self.rear
    def enqueue(self,x):
        t=Node(x)
        if self.empty():
            self.front=t
            self.rear=t
            self.size+=1
        else:
            self.rear.next=t
            self.rear=t
            self.size+=1
    def dequeue(self):
        if self.empty():
            return "UNDERFLOW"
        else:
            t=self.front
            self.front=self.front.next
            x=t.val
            t=None
            self.size-=1
            return x
    def printl(self):
        t=self.front
        while t!=None:
            print(t.val,end="--->")
            t=t.next
        print("NULL")

q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.printl()
print(q.dequeue())
q.printl()
print(q.dequeue())
q.enqueue(40)
print(q.dequeue())
q.printl()

