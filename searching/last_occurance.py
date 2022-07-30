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

if __name__ =="__main__":
    arr=[5,10,10,10,10,20,20]
    x=10
    print(last(arr,x))