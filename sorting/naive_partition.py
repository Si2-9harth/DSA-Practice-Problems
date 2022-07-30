def partition(arr,l,h,p):
    n=h-l+1
    temp=[0]*n
    index=0
    for i in range(l,h+1):
        if arr[i]<arr[p]:
            temp[index]=arr[i]
            index=index+1

    for i in range(l,h+1):
        if arr[i] == arr[p]:
           temp[index]=arr[i]
           index=index+1  
    res=l+index-1

    for i in range(l,h+1):
        if arr[i]>arr[p]:
            temp[index]=arr[i]
            index=index+1
    
    for i in range(l,h+1):
        arr[i]=temp[i-l]

    return res  
        

arr=[5,3,12,8,5]
l=0
h=4
p=0
print(partition(arr,l,h,p))
print(arr)