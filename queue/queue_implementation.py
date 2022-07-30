class queue:
    def __init__(self,c):
        self.capacity = c
        self.arr=[None]*self.capacity
        self.size=0
    def full(self):
        return self.size==self.capacity
    def empty(self):
        return self.size==0
    def enqueue(self,x):
        if self.full():
            print("OVERFLOW!!!")
        else:
            self.arr.insert(self.size,x)
            self.size+=1
    def dequeue(self):
        if self.empty():
            print("UNDERFLOW!!!")
            return
        else:
            t=self.arr[0]
            self.arr.pop(0)
            self.size-=1
            return t
    def getfront(self):
        if self.empty():
            return-1
        else:
            return 0
    def getrear(self):
        if self.empty():
            return -1
        else:
            return self.size-1

q=queue(3)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
print(q.dequeue())
q.enqueue(40)
print(q.dequeue())
print(q.arr)
    