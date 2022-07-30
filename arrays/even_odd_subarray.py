def longest(arr):
    n=len(arr)
    res=1
    for i in range(n):
        cur=1
        for j in range(i+1,n):
            if (arr[j]%2==0 and arr[j-1]%2!=0) or (arr[j-1]%2==0 and arr[j]%2!=0):
                cur=cur+1
            else:
                break
        res=max(res,cur)
    return res

def longestt(arr):
    n=len(arr)
    res=1
    cur=1
    for i in range(1,n):
        if (arr[i-1]%2==0 and arr[i]%2!=0) or (arr[i]%2==0 and arr[i-1]%2!=0):
            cur=cur+1
            res=max(res,cur)
        else:
            cur=1
    return res

    
if __name__ == '__main__':
    arr=[5,10,20,6,3,8]
    print(longestt(arr))