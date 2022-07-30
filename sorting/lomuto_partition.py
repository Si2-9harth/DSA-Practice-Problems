def lomuto(arr,l,h):
    pivot=arr[h]
    i=-1
    for j in range(h):
        if arr[j]<pivot:
            i=i+1
            t=arr[j]
            arr[j]=arr[i]
            arr[i]=t
    t=arr[h]
    arr[h]=arr[i+1]
    arr[i+1]=t        
    return i+1

arr=[10,80,30,90,40,50,70]
l=0
h=len(arr)-1
print(lomuto(arr,l,h))
print(arr)