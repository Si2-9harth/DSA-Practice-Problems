def countM(arr,l,r,m):
    n1=m-l+1
    n2=r-m
    L=[0]*n1
    R=[0]*n2
    for i in range(n1):
        L[i]=arr[l+i]
    for i in range(n2):
        R[i]=arr[m+1+i]
    i=0
    j=0
    k=l
    res=0 
    while i<n1 and j<n2:
        if L[i]>R[j]:
            arr[k]=R[j]
            res=res+n1-i
            j=j+1
            k=k+1
        else:
            arr[k]=L[i]
            i=i+1
            k=k+1
    
    while i<n1:
        arr[k]=L[i]
        i=i+1
        k=k+1
    while j<n2:
        arr[k]=R[j]
        j=j+1
        k=k+1

    return res


def countI(arr,l,r):
    res=0
    if l<r:
        m=l+(r-l)//2
        res+=countI(arr,l,m)
        res+=countI(arr,m+1,r)
        res+=countM(arr,l,r,m)
    return res

a=[2,4,1,3,5]
print(countI(a,0,len(a)-1))