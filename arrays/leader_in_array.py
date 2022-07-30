def leaders(arr):
    for i in range(len(arr)):
        flag=False
        for j in range(i+1,len(arr)):
            if arr[j]>=arr[i]:
                flag=True
                break
        if flag==False:
            print(arr[i],end=" ")
    return

def leaderss(arr):
    n=len(arr)
    print(arr[n-1],end=" ")
    cur=arr[n-1]   
    for i in range(n-2,-1,-1):
        if arr[i]>cur:
            print(arr[i],end=" ")
            cur=arr[i]
    return 

if __name__ == '__main__':
    leaderss([30,10,20])