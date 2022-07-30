from re import L


def max_guests(arr,dep):
    arr.sort()
    dep.sort()
    i=1
    j=0
    cur=1
    res=1
    while i<len(arr) and j<len(dep):
        if arr[i]<=dep[j]:
            i=i+1
            cur=cur+1
            res=max(res,cur)
        else:
            cur=cur-1
            j=j+1
    return res

arr=[900,600,700]
dep=[1000,800,730]
print(max_guests(arr,dep))