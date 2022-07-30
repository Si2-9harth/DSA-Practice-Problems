def sort_two_types(arr,n):
    j=n
    i=-1
    while True:
        i=i+1
        while(arr[i]<0):
            i=i+1
        j=j-1
        while (arr[j]>0):
            j=j-1
        if i>=j:
            return
        arr[j],arr[i]=arr[i],arr[j]        

arr=[-12,18,-10,15]
sort_two_types(arr,len(arr))
print(arr)