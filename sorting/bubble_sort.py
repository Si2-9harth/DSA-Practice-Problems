def bubble(arr):
    n=len(arr)
    for i in range(n-1):
        f=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                t=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=t
                f=True
        if f==False:
            break
    return arr

if __name__ =="__main__":
    arr=[10,8,20,5]
    print(bubble(arr))