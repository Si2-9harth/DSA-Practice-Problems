def first(arr,x,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]>x:
        return first(arr,x,low,mid-1)
    elif arr[mid]<x:
        return first(arr,x,mid+1,high)
    else:
        if mid==0 or arr[mid-1]!=arr[mid]:
            return mid
        else:
            return first(arr,x,low,mid-1)

def firstt(arr,x):
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

if __name__ =="__main__":
    arr=[5,10,10,15,20,20,20]
    x=20
    print(firstt(arr,x))