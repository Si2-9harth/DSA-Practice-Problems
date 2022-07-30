def naive(arr,n,k):
    if k==1:
        return sum_pages(arr,0,n-1)
    if n==1:
        return arr[0]
    res=float('inf')
    for i in range(n):
        res=min(res,max(sum_pages(arr,i,n-1),naive(arr,i,k-1)))
    return res


def sum_pages(arr,start,stop):
    s=0
    for i in range(start,stop+1):
        s=s+arr[i]
    return s


def feasible(arr,ans,k):
    req=1
    s=0
    for i in range(len(arr)):
        if arr[i]+s>ans:
            s=arr[i]
            req+=1
        else:
            s=arr[i]+s
    
    return req<=k

def min_pages(arr,n,k):
    sum=0
    mx=0
    res=0
    for i in range(n):
        sum+=arr[i]
        mx=max(mx,arr[i])
    
    low=mx
    high=sum
    while low<=high:
        mid=(low+high)//2
        if feasible(arr,mid,k):
            high=high-1  
            res=mid
        else:
            low=low+1
    return res

if __name__ =="__main__":
    arr=[10,5,30,1,2,5,10,10]
    n=len(arr)
    k=3
    print(min_pages(arr,n,k))