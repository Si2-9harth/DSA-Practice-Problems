def insertion(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while (j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

if __name__ =="__main__":
    arr=[20,5,40,60,10,30]
    print(insertion(arr))