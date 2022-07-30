def max_sum(arr):
    res=arr[0]
    for i in range(len(arr)):
        cur=0
        for j in range(i,len(arr)):
            cur=cur+arr[j]
            res=max(cur,res)
    return res

def max_summ(arr):
    res=arr[0]
    max_ending=arr[0]
    n=len(arr)
    for i in range(n):
        max_ending=max(max_ending+arr[i],arr[i])
        res=max(res,max_ending)
    return res
if __name__ == "__main__":
    print(max_summ([1,-2,3,-1,2]))