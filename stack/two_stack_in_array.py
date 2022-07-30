class twoStacks:
    def __init__(self,cap):
        self.n=cap
        self.top1=-1
        self.top2=self.n
        self.arr=[None]*self.n
    
    def push1(self,x):
        if self.top1<self.top2-1:
            self.top1+=1
            self.arr[self.top1]=x
        else:
            print("OVERFLOW!!!")
    
    def push2(self,x):
        if self.top1<self.top2-1:
            self.top2-=1
            self.arr[self.top2]=x
        else:
            print("OVERFLOW!!!")

    def pop1(self):
        if self.top1==-1:
            print("UNDERFLOW!!!")
        else:
            print(self.arr[self.top1])
            self.arr[self.top1]=None
            self.top1-=1
    
    def pop2(self):
        if self.top2==self.n:
            print("UNDERFLOW!!!")
        else:
            print(self.arr[self.top2])
            self.arr[self.top2]=None
            self.top2+=1
    def size1(self):
        return self.top1+1

    def size2(self):
        return self.n-self.top2

ts = twoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)
print(ts.arr)
ts.pop2()
ts.pop1()
print(ts.arr)
print(ts.size1())
print(ts.size2())