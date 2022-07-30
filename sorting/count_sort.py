def count_sort(arr,k,n):
    count=[0]*k
    for i in range(n):
        count[arr[i]]+=1
    for i in range(1,k):
        count[i]=count[i-1]+count[i]
    op=[0]*n
    i=n-1
    while i>=0:
        op[count[arr[i]]-1]=arr[i]
        count[arr[i]]-=1
        i=i-1
    for i in range(n):
        arr[i]=op[i]

def count_sort_abc(arr):
    op=[""]*len(arr)
    count=[0]*256
    ans=[""]*len(arr)
    for i in range(len(arr)):
        count[ord(arr[i])]+=1
    for i in range(1,256):
        count[i]=count[i-1]+count[i]
    n=len(arr)
    for i in range(n-1,-1,-1):
        op[count[ord(arr[i])]-1]=arr[i]
        count[ord(arr[i])]-=1

    for i in range(n):
        ans[i]=op[i]
    return ans


arr=[5,6,5,2]
k=7
count_sort(arr,k,len(arr))
print(arr)
brr="geeksforgeeks"
print("".join(count_sort_abc(brr)))
