def cycle_sort(arr):
    n=len(arr)
    for cs in range(n-1):
        item=arr[cs]
        pos=cs
        for i in range(cs+1,n):
            if arr[i]<item:
                pos+=1
        arr[pos],item=item,arr[pos]
        while pos!=cs:
            pos=cs
            for i in range(cs+1,n):
                if arr[i]<item:
                    pos+=1
            arr[pos],item=item,arr[pos]

arr=[20,40,50,10,30]
cycle_sort(arr)
print(arr)