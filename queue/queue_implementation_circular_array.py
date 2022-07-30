class queue:
    def __init__(self,capacity):
        self.capacity=capacity
        self.arr=[None]*self.capacity
        self.size=0
        self.front=0
    def full(self):
        return self.size==self.capacity
    def empty(self):
        return self.size==0
    def enqueue(self,x):
        if self.full():
            print("OVERFLOW")
            return
        else:
            rear=(self.front+self.size-1)%self.capacity
            rear=(rear+1)%self.capacity
            self.arr[rear]=x
            self.size+=1
    def dequeue(self):
        if self.empty():
            return
        else:
            t=self.arr[self.front]
            self.arr[self.front]=None
            self.front=(self.front+1)%self.capacity
            self.size-=1
            return t
    def front(self):
        if self.empty():
            return -1
        else:
            return self.front
    def rear(self):
        if self.empty():
            return -1
        else:
            return (self.front+self.size-1)%self.capacity

q=queue(3)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.arr)
print(q.dequeue())
print(q.arr)
print(q.dequeue())
print(q.arr)
q.enqueue(40)
print(q.arr)
print(q.dequeue())
print(q.arr)