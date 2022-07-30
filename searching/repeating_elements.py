def repeating(arr):
    n=len(arr)
    ba=[False]*(n-1)
    for i in range(n):
        if ba[arr[i]]==False:
            ba[arr[i]]=True
        else:
            return arr[i]

def efficient(arr):
    for i in range(len(arr)):
        arr[i]=arr[i]+1
    slow=arr[0]
    fast=arr[0]

    slow=arr[slow]
    fast=arr[arr[fast]]

    while slow!=fast:
        slow=arr[slow]
        fast=arr[arr[fast]]
    
    
    slow=arr[0]

    while slow!=fast:
        slow=arr[slow]
        fast=arr[fast]
    return slow-1

if __name__ == "__main__":
    arr=[0,2,1,3,2,2]
    print(efficient(arr))