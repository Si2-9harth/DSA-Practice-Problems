def bucket_sort(arr,k):
    mx=max(arr)+1
    bkt=[]
    for i in range(k):
        a=[]
        bkt.append(a)
    for i in range(len(arr)):
        bi=(k*arr[i])//mx
        bkt[bi].append(arr[i])
    for i in bkt:
        i.sort()
    index=0
    for i in bkt:
        for j in range(len(i)):
            arr[index]=i[j]
            index+=1

arr=[30,40,10,80,5,12,70]
k=4
bucket_sort(arr,k)
print(arr)