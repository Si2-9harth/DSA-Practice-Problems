def check(arr,k):
    i=0
    cur=0
    s=0
    while i<len(arr):
        if s==k:
            return True
        elif s<k:
            s=s+arr[i]
            i=i+1
        else:
            s=s-arr[cur]
            if s==0:
                i=i+1
                s=s+arr[i]
                cur=i
            else:
                cur=cur+1
    return False

def checks(arr,k):
    n=len(arr)
    arr_sum=arr[0]
    s=0
    for e in range(1,n):
        while arr_sum>k and s<e-1:
            arr_sum=arr_sum-arr[s]
            s=s+1
        if arr_sum==k:
            return True
        if e<n:
            arr_sum=arr_sum+arr[e]
    return arr_sum==k


if __name__ =="__main__":
    arr=[1,4,20,3,10,5]
    k=15
    print(checks(arr,k))