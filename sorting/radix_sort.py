def counting_sort(arr,n,exp):
    count=[0]*10
    op=[0]*n
    for i in range(n):
        count[(arr[i]//exp)%10]+=1
    for i in range(1,10):
        count[i]=count[i-1]+count[i]
    i=n-1
    while i>=0:
        op[count[(arr[i]//exp)%10]-1]=arr[i]
        count[(arr[i]//exp)%10]-=1
        i=i-1

    for i in range(n):
        arr[i]=op[i]

def radix_sort(arr):
    mx=max(arr)
    n=len(arr)
    exp=1
    while mx//exp>0:
        counting_sort(arr,n,exp)
        exp*=10

arr=[319,212,6,8,100,50]
radix_sort(arr)
print(arr)