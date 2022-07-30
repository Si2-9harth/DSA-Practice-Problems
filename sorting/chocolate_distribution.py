def merge(arr,l,h,m):
    n1=m-l+1
    n2=h-m
    L=[0]*n1
    R=[0]*n2
    for i in range(n1):
        L[i]=arr[l+i]
    for i in range(n2):
        R[i]=arr[m+i+1]
    
    i=0
    j=0
    k=l 
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[k]=L[i]
            i=i+1
        else:
            arr[k]=R[j]
            j=j+1
        k=k+1
    
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
        p=l+(h-l)//2
        merge_sort(arr,l,p)
        merge_sort(arr,p+1,h)
        merge(arr,l,h,p)

def minDif(arr,n,m):
    if m>n:
        return -1
    elif m==n:
        return max(arr)-min(arr)
    else:
        merge_sort(arr,0,n-1)
        i=0
        res=arr[m-1]-arr[0]
        while i+m-1<n:
            res=min(res,arr[m+i-1]-arr[i])
            i=i+1
        return res

arr=[7,3,2,4,9,12,56]
m=3
merge_sort(arr,0,len(arr)-1)
print(arr)
print(minDif(arr,len(arr),m))