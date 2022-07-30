def merge(arr,l,h,mid):
    n1=mid-l+1
    n2=h-mid
    L=[0]*n1
    R=[0]*n2
    for i in range(n1):
        L[i]=arr[l+i]
    for i in range(n2):
        R[i]=arr[mid+i+1]
    i=0
    j=0
    k=l 
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1  
    while i<n1:
        arr[k]=L[i]
        i=i+1
        k=k+1
    while j<n2:
        arr[k]=R[j]
        j=j+1
        k=k+1


def merge_sort(arr,l,h):
    if l<h:
        mid=l+(h-l)//2
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,h)
        merge(arr,l,h,mid)

def min_diff(arr):
    n=len(arr)
    if n<=1:
        return float('inf')
    elif n==2:
        return max(arr)-min(arr)
    else:
        res=float('inf')
        merge_sort(arr,0,n-1)
        for i in range(1,n):
            res=min(res,arr[i]-arr[i-1])
        return res

arr=[10,8,1,4]
print(min_diff(arr))
print(arr)