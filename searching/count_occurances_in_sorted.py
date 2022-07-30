def first(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
        else:
            if mid==0 or arr[mid-1]!=arr[mid]:
                return mid
            else:
                high=mid-1
    return -1

def last(arr,x):
    low=0
    n=len(arr)
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
        else:
            if mid==n-1 or arr[mid]!=arr[mid+1]:
                return mid
            else:
                low=mid+1 

def counts(arr,x):
    f=first(arr,x)
    if f<0:
        return 0
    else:
        return last(arr,x)-f+1

if __name__ =="__main__":
    arr=[10,20,20,20,40,40]
    x=20
    print(counts(arr,x))