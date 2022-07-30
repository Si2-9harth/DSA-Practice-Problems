def get_largest(arr):
    res=0
    for i in range(len(arr)):
        cur=arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]>=arr[i]:
                cur+=arr[i]
            else:
                break
        for j in range(i+1,len(arr)):
            if arr[j]>=arr[i]:
                cur+=arr[i]
            else:
                break
        res=max(res,cur)

    return res

class stack:
    def __init__(self):
        self.arr=[]
    def push(self,val):
        self.arr.append(val)
    def isempty(self):
        return self.arr==[]
    def pop(self):
        if self.isempty():
            print("UNDERFLOW!!!")
        else:
            return self.arr.pop()
    def top(self):
        return self.arr[-1]
    def size(self):
        return len(self.arr)

def previous_small(arr):
    a=[]
    s=stack()
    s.push(0)
    a.append(-1)
    for i in range(1,len(arr)):
        while s.isempty()==False and arr[i]<=arr[s.top()]:
            s.pop()
        if s.isempty():
            a.append(-1)
        else:
            a.append(s.top())
        s.push(i)
    return a
def next_small(arr):
    s=stack()
    n=len(arr)
    a=[None]*(n)
    s.push(n-1)
    a[n-1]=n
    for i in range(n-2,-1,-1):
        while s.isempty()==False and arr[i]<=arr[s.top()]:
            s.pop()
        if s.isempty():
            a[i]=n
        else:
            a[i]=s.top()
        s.push(i)
    return a

def gett_largest(arr):
    ns=next_small(arr)
    ps=previous_small(arr)
    #print(ns)
    #print(ps)
    res=0
    for i in range(len(arr)):
        cur=arr[i]
        cur+=arr[i]*(i-ps[i]-1)
        cur+=arr[i]*(ns[i]-i-1)
        res=max(res,cur)
    return res

def gett_largestt(arr):
    n=len(arr)
    s=stack()
    res=0
    for i in range(len(arr)):
        while s.isempty()==False and arr[s.top()]>=arr[i]:
            tp=s.pop()
            if s.isempty():
                x=i
            else:
                x=i-s.top()-1
            cur=arr[tp]*x
            res=max(res,cur)
        s.push(i)
    while s.isempty()==False:
        tp=s.pop()
        if s.isempty():
            x=n
        else:
            x=n-s.top()-1
        cur=arr[tp]*x
        res=max(res,cur)
    return res

print(get_largest([6,2,5,4,1,5,6]))
print(gett_largest([6,2,5,4,1,5,6]))
print(gett_largestt([6,2,5,4,1,5,6]))