def pair(arr,x):
    low=0
    n=len(arr)
    high=n-1
    while low<high:
        if arr[low]+arr[high]==x:
            return True
        elif arr[low]+arr[high]>x:
            high=high-1
        else:
            low=low+1
    return False

if __name__ == "__main__":
    arr=[2,4,8,9,11,12,20,30]
    x=23
    print(pair(arr,x))