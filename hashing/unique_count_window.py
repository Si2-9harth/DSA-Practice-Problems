def unique_counts(arr,k):
    n=len(arr)
    m=dict()
    for i in range(k):
        if arr[i] not in m.keys():
            m[arr[i]]=1
        else:
            m[arr[i]]+=1
    print(len(m),end=" ")
    for i in range(k,n):
        m[arr[i-k]]-=1
        if m[arr[i-k]]==0:
            del m[arr[i-k]]
        if arr[i] not in m.keys():
            m[arr[i]]=1
        else:
            m[arr[i]]+=1
        print(len(m),end=" ")



arr=[10, 10, 5, 3, 20, 5]
k=4
unique_counts(arr,k)