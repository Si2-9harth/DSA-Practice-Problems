def ceil_left(arr):
    s=set()
    for i in range(len(arr)):
        it=[j for j in s if j>=arr[i]]
        if len(it)==0:
            print(-1,end=" ")
        else:
            print(min(it),end=" ")
        s.add(arr[i])


arr=[2,8,30,15,25,12]
ceil_left(arr)