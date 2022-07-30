def dutch(arr,n):
    mid=0
    l=0
    h=n-1
    while mid<=h:
        if arr[mid]==0:
            arr[mid],arr[l]=arr[l],arr[mid]
            l=l+1
            mid=mid+1
        elif arr[mid]==1:
            mid=mid+1
        else:
            arr[mid],arr[h]=arr[h],arr[mid]
            h=h-1


arr=[0,1,2,1,1,2,0]
dutch(arr,len(arr))
print(arr)