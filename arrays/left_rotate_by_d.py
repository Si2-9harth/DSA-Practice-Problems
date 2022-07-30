def rotate(arr):
    t=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]=t
    return arr

def rotate_d(arr,d):
    for i in range(d):
        arr=rotate(arr)
    return arr

def rotate_dd(arr,d):
    t=arr[:d]
    n=len(arr)
    for i in range(d,len(arr)):
        arr[i-d]=arr[i]
    arr=arr[:n-d]+t
    return arr

def reverse(a,low,high):
    while high>low:
        t=a[high]
        a[high] = a[low]
        a[low] = t
        high=high-1
        low=low+1
    return a

def rotate_ddd(arr,d):
    n=len(arr)
    arr=reverse(arr,0,d-1)
    arr=reverse(arr,d,n-1)
    arr=reverse(arr,0,n-1)
    return arr

if __name__ == '__main__':
    print(rotate_dd([1,2,3,4,5,6],2))