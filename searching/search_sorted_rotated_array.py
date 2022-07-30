def search(arr,x):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid 
        elif arr[low]<arr[mid]:
            if arr[low]<=x and arr[mid]>x:
                high=mid-1
            else:
                low=mid+1  
        else:
            if arr[high]>=x and arr[mid]<x:
                low=mid+1  
            else:
                high=mid-1
    return -1

if __name__ == '__main__':
    arr=[10,20,40,60,5,8]
    x=5
    print(search(arr,x))