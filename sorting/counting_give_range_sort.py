def count_sort(arr,mn,mx):
    k=mx-mn+1
    n=len(arr)
    count=[0]*k
    op=[0]*n
    for i in range(n):
        count[arr[i]-mn]+=1
    for i in range(1,k):
        count[i]=count[i-1]+count[i]
    for i in range(n-1, -1, -1):
        op[count[arr[i]-mn]-1]=arr[i]
        count[arr[i]-mn]-=1
 
    for i in range(0,n):
        arr[i]=op[i]

    return arr

arr=[-2,2,-1,0,1,6,1,5,8,10,9]
mi=-3
ma=10
ans=count_sort(arr,mi,ma)
print(ans)