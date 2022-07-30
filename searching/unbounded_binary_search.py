def binary_search(arr,x,low,high):
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return -1


def bs(arr,x):
    if arr[0]==x:
        return 0
    else:
        i=1
        while arr[i]<x:
            if arr[i]==x:
                return i
            i=i*2
        return binary_search(arr,x,i//2+1,i-1)



if __name__ =="__main__":
    arr=[1,10,15,20,40,60,80,100,200,500,1000,2000,2400,124124]
    print(bs(arr,100))