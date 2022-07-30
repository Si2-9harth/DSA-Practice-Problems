def binary_search(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return -1

if __name__ =="__main__":
    arr=[10,20,30,40,50,60,70]
    x=60
    print(binary_search(arr,x))