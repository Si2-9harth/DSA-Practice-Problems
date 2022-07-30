def greedy(arr):
    a=sorted(arr,key=lambda x:x[-1])
    prev=0
    res=1
    for i in range(1,len(a)):
        if a[prev][-1]<=a[i][0]:
            res+=1
            prev=i
    return res


arr=[[12,25],[13,20],[20,30]]
print(greedy(arr))