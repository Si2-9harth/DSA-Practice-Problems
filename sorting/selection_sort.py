def selection(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[mini]>arr[j]:
                mini=j
        t=arr[mini]
        arr[mini]=arr[i]
        arr[i]=t
    return arr

if __name__ =="__main__":
    arr=[10,5,8,20,2,18]
    print(selection(arr))