def longest_sorting(arr):
    arr.sort()
    res=1
    cur=1
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]+1:
            cur+=1
        elif arr[i]!=arr[i-1]:
            res=max(res,cur)
            cur=1
    return max(res,cur)

def longest(arr):
    s=set(arr)
    res=1
    for i in s:
        if i-1 not in s:
            cur=1
            while i+cur in s:
                cur+=1
        res=max(res,cur)
    return res



arr=[2,9,4,3,10]
print(longest_sorting(arr))
print(longest(arr))