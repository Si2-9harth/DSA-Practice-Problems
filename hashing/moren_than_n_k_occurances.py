def n_k_occurances(arr,k):
    n=len(arr)
    m=dict()
    val=n/k
    for i in range(n):
        if arr[i] not in m.keys():
            m[arr[i]]=1
        else:
            m[arr[i]]+=1
    for i in m.keys():
        if m[i]>val:
            print(i,end=" ")
    return 
def n_by_k(arr,k):
    n=len(arr)
    m=dict()
    for i in range(n):
        if arr[i] in m.keys():
            m[arr[i]]+=1
        elif len(m)<k-1:
            m[arr[i]]=1
        else:
            for i in m.copy().keys():
                m[i]-=1
                if m[i]==0:
                    del m[i]
    for i in m.keys():
        count=0
        for j in arr:
            if j==i:
                count+=1
        if count>n/k:
            print(i,end=" ")



arr=[10,10,20,20,20,20,30,20,10,10]
k=4
n_k_occurances(arr,k)
n_by_k(arr,k)