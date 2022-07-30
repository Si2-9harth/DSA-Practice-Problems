class stacks:
    def __init__(self,cap,k):
        self.n=cap
        self.k=k
        self.arr=[None]*self.n
        self.next=[None]*self.n
        self.top=[-1]*self.k
        for i in range(self.n):
            self.next[i]=i+1
        self.next[self.n-1]=-1
        self.freetop=0
    
    def push(self,val,sn):
        if self.freetop==-1:
            print("OVERFLOW!!!")
        else:
            i=self.freetop
            self.freetop=self.next[i]
            self.arr[i]=val
            self.next[i]=self.top[sn]
            self.top[sn]=i
    
    def pop(self,sn):
        if self.top[sn]==-1:
            print("UNDERFLOW!!!")
        else:
            i=self.top[sn]
            print(self.arr[i])
            self.arr[i]=None
            self.top[sn]=self.arr[i]
            self.next[i]=self.freetop
            self.freetop=i
    
ks=stacks(10,3)
print(ks.top)
print(ks.arr)
print(ks.next)
ks.push(15, 2) 
ks.push(45, 2)
ks.push(17, 1) 
ks.push(49, 1) 
ks.push(39, 1) 
ks.push(11, 0)
ks.push(9, 0)
ks.push(7, 0)
print(ks.arr)
ks.pop(2)
print(ks.arr)
ks.pop(1)
ks.pop(0)       
print(ks.arr)