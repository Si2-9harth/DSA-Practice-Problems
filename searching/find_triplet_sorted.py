def pair(arr,x,low,high):
    while low<high:
        if arr[low]+arr[high]==x:
            return True
        elif arr[low]+arr[high]>x:
            high=high-1
        else:
            low=low+1
    return False 


def triplet(arr,x):
    n=len(arr)
    for i in range(len(arr)):
        if pair(arr,x-arr[i],i+1,n-1):
            return True
    return False

if __name__ =="__main__":
    arr=[2,3,4,8,9,20,40]
    x=32
    print(triplet(arr,x))