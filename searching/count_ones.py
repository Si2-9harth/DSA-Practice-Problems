def counts(arr):
    low=0
    n=len(arr)
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<1:
            low=mid+1
        else:
            if mid==0 or arr[mid-1]!=1:
                return n-mid
            else:
                high=mid-1
    return 0


if __name__ =="__main__":
    arr=[0,0,0]
    print(counts(arr))