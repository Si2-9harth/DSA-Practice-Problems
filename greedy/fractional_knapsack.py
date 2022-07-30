class pair:
    def __init__(self,w,v):
        self.w=w
        self.v=v

def greedy(arr,cap):
    a=sorted(arr,key=lambda x:x.v/x.w,reverse=True)
    res=0
    for i in a:
        if i.w<=cap:
            res=res+i.v
            cap=cap-i.w
        else:
            res=res+(i.v*(cap/i.w))
            break
    return res

arr=[]
arr.append(pair(30,120))
arr.append(pair(20,100))
arr.append(pair(10,60))
print(greedy(arr,50))