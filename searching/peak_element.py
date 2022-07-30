def naive(arr):
    n=len(arr)
    if n==0:
        return 0
    if arr[0]>=arr[1]:
        return 0
    if arr[n-1]>=arr[n-2]:
        return n-1
    for i in range(1,n-1):
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
            return i

def efficient(arr):
    n=len(arr)
    low=0
    high=n-1                  
    while low<=high:
        mid=(low+high)//2
        if (mid==0 or arr[mid]>=arr[mid-1]) and (mid==n-1 or arr[mid]>=arr[mid+1]):
            return mid  
        elif mid>0 and arr[mid-1]>=arr[mid]:
            high=mid-1 
        else:
             low=mid+1   

if __name__ == '__main__':
    arr=[10,7,8,20,12]
    print(efficient(arr))