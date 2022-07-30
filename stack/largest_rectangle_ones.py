class stack:
    def __init__(self):
        self.arr=[]
    def push(self,val):
        self.arr.append(val)
    def isempty(self):
        return self.arr==[]
    def top(self):
        return self.arr[-1]
    def pop(self):
        if self.isempty():
            print("UNDERFLOW!!!")
        else:
            return self.arr.pop()

def largest_rectangle(arr):
    n=len(arr)
    s=stack()
    res=0
    for i in range(n):
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

def largest(mat):
    r=len(mat)
    c=len(mat[0])
    res=largest_rectangle(mat[0])
    for i in range(1,r):
        for j in range(c):
            if mat[i][j]==1:
                mat[i][j]+=mat[i-1][j]
        res=max(res,largest_rectangle(mat[i]))
    return res

print(largest([[1,0,0,1,1],[0,0,0,1,1],[1,1,1,1,1],[0,1,1,1,1]]))