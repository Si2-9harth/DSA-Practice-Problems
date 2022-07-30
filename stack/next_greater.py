class stack:
    def __init__(self):
        self.arr=[]
    
    def push(self,val):
        self.arr.append(val)
    
    def pop(self):
        if self.arr==[]:
            print("ERROR")
        else:
            self.arr.pop()
    
    def top(self):
        return self.arr[-1]
    
    def size(self):
        return len(self.arr)
    
    def isempty(self):
        return self.arr==[]

def next_g(arr):
    s=stack()
    s.push(arr[-1])
    t=[]
    t.append(-1)
    for i in range(len(arr)-2,-1,-1):
        while s.isempty()==False and arr[i]>=s.top():
            s.pop()
        if s.isempty():
            t.append(-1)
        else:
            t.append(s.top())
        s.push(arr[i])
    return t

x=next_g([5,15,10,8,6,12,9,18])
print(x[::-1])
#15,18,12,12,12,18,18,-1