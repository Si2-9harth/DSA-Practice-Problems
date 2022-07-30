class pair:
    def __init__(self,deadline,profit):
        self.profit=profit
        self.deadline=deadline

def greedy(arr):
    arr.sort(key=lambda x:x.profit,reverse=True)
    m=0
    for i in arr:
        m=max(m,i.deadline)
    
    res=[0]*m
    for i in arr:
        d=i.deadline
        if res[d-1]==0:
            res[d-1]=i.profit
        else:
            j=d-1
            while j>=0:
                if res[j]==0:
                    res[j]=i.profit
                    break
                j=j-1
    return sum(res) 

arr=[]
arr.append(pair(2,100))
arr.append(pair(1,50))
arr.append(pair(2,10))
arr.append(pair(1,20))
arr.append(pair(3,30))
print(greedy(arr))
#180