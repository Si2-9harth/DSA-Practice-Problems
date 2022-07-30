def max_sum(arr,k):
    n=len(arr)
    maxs=float('-inf')
    for i in range(n-k+1):
        s=0
        for j in range(k):
            s+=arr[i+j]
        maxs=max(maxs,s)
    return maxs

def sliding(arr,k):
    cur=0
    n=len(arr)
    for i in range(k):
        cur+=arr[i]
    maxs=cur
    for i in range(k,n):
        cur=cur+(arr[i]-arr[i-k])
        maxs=max(cur,maxs)
    return maxs


if __name__ == '__main__':
    arr=[1,8,30,-5,20,7]
    k=3
    print(sliding(arr,k))