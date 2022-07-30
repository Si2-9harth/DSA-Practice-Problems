class queue:
    def __init__(self):
        self.arr=[]
        self.size=0
    def empty(self):
        return self.arr==[]
    def front(self):
        return self.arr[0]
    def rear(self):
        return self.arr[-1]
    def push(self,val):
        self.arr.append(val)
        self.size+=1
    def pop(self):
        if self.empty():
            return
        else:
            t=self.arr.pop(0)
            self.size-=1
            return t
    def size(self):
        return len(self.arr)

class stack:
    def __init__(self):
        self.arr=[]
    def empty(self):
        return self.arr==[]
    def push(self,val):
        self.arr.append(val)
    def pop(self):
        if self.empty()==True:
            return
        else:
            return self.arr.pop()
    def top(self):
        return self.arr[-1]

def reverse(q):
    s=stack()
    while q.empty()==False:
        s.push(q.front())
        q.pop()
    while s.empty()==False:
        q.push(s.top())
        s.pop()
    return q
  
def reverser(q):
    if q.empty()==True:
        return
    else:
        x=q.front()
        q.pop()
        reverser(q)
        q.push(x)

q=queue()
q.push(10)
q.push(20)
q.push(30)
q.push(40)
q.push(50)
reverser(q)
print(q.arr)
