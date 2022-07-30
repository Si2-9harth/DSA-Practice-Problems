def water(arr):
    res=0
    for i in range(1,len(arr)-1):
        lmax=arr[0]
        rmax=arr[i]
        for j in range(i):
            lmax=max(arr[j],lmax)
        for j in range(i+1,len(arr)):
            rmax=max(arr[j],rmax)
        res+=min(rmax,lmax)-arr[i]
    return res

def waterr(arr):
    n=len(arr)
    res=0
    lmax=[0]*n
    rmax=[0]*n
    lmax[0]=arr[0]
    rmax[n-1]=arr[n-1]
    for i in range(1,n):
        lmax[i]=max(lmax[i-1],arr[i])
    for i in range(n-2,-1,-1):
        rmax[i]=max(arr[i],rmax[i+1])
    for i in range(1,n-1):
        res=res+min(lmax[i],rmax[i])-arr[i]
    return res

if __name__ == '__main__':
    arr=[3,0,1,2,5]
    print(waterr(arr))