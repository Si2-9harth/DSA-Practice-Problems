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

def span(arr):
    s=stack()
    s.push(0)
    print(1,end=" ")
    for i in range(1,len(arr)):
        while s.isempty()==False and arr[i]>=arr[s.top()]:
            s.pop()
        if s.isempty==True:
            print(i+1,end=" ")
        else:
            print(i-s.top(),end=" ")
        s.push(i)

span([60,10,20,15,35,50])