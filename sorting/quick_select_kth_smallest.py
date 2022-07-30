import random
def partition(arr,l,r):
    p=random.randint(l,r)
    arr[r],arr[p]=arr[p],arr[r]
    pivot=arr[r]
    i=l-1
    for j in range(l,r):
        if arr[i]<pivot:
            i=i+1
            arr[j],arr[i]=arr[i],arr[j]
    arr[r],arr[i+1]=arr[i+1],arr[r]
    return i+1

def quick_select(arr,n,k):
    if k>n:
        return -1
    else:
        l=0
        r=n-1
        while l<=r:
            p=partition(arr,l,r)
            if p==k-1:
                return arr[p]
            elif p>k-1:
                r=p-1
            else:
                l=p+1


arr=[30,20,5,10,8]
k=4
n=len(arr)
print(quick_select(arr,n,k))