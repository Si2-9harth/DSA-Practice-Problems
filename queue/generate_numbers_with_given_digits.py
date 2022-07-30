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

def nums(a,b,num):
    q=queue()
    q.push(a)
    q.push(b)
    c=0
    while c<num:
        cur=q.front()
        cur=str(cur)
        print(cur,end=" ")
        q.pop()
        q.push(cur+"{}".format(a))
        q.push(cur+"{}".format(b))
        c+=1

num=10
a=5
b=6
nums(a,b,num)