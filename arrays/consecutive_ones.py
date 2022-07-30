def counts(arr):
    n=len(arr)
    res=0
    for i in range(n):
        cur=0
        for j in range(i,n):
            if arr[j]==1:
                cur+=1
            else:
                break
        res=max(res,cur)
    return res

def countss(arr):
    n=len(arr)
    res=0
    for i in range(n):
        if arr[i]==0:
            cur=0
        else:
            cur=cur+1
            res=max(res,cur)
    return res

if __name__ == "__main__":
    print(countss([0,1,1,1,0,1,1]))       