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

def previous_g(arr):
    s=stack()
    s.push(arr[0])
    print(-1,end=" ")
    for i in range(1,len(arr)):
        while s.isempty()==False and arr[i]>=s.top():
            s.pop()
        if s.isempty():
            print(-1,end=" ")
        else:
            print(s.top(),end=" ")
        s.push(arr[i])


previous_g([15,10,18,12,4,6,2,8])