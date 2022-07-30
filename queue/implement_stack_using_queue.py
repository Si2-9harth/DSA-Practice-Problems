class queue:
    def __init__(self):
        self.size=0
        self.arr=[]
    def empty(self):
        return self.arr==[]
    def push(self,val):
        self.arr.append(val)
        self.size+=1
    def pop(self):
        if self.empty():
            return
        else:
            t=self.arr[0]
            self.arr.pop(0)
            return t
    def front(self):
        return self.arr[0]
    def rear(self):
        return self.arr[-1]
    def size(self):
        return len(self.arr)

class stack:
    def __init__(self):
        self.q1=queue()
        self.q2=queue()
    def top(self):
        return self.q1.front()
    def pop(self):
        return self.q1.pop()
    def push(self,x):
        while self.q1.empty()==False:
            self.q2.push(self.q1.front())
            self.q1.pop()
        self.q1.push(x)
        while self.q2.empty()==False:
            self.q1.push(self.q2.front())
            self.q2.pop()

s=stack()
s.push(10)
s.push(20)
s.push(30)
print(s.q1.arr)
print(s.top())
print(s.pop())
print(s.q1.arr)