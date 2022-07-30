def longest(arr,sum):
    res=0
    prefix_sum=0
    d=dict()
    for i in range(len(arr)):
        prefix_sum+=arr[i]
        if prefix_sum==sum:
            res=i+1 
        if prefix_sum not in d.keys():
            d[prefix_sum]=i
        if prefix_sum-sum in d.keys():
            res=max(res,i-d[prefix_sum-sum])
    return res

def longestoz(arr):
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=-1
    return longest(arr,0)

arr=[1,1,1,0,1,0]
print(longestoz(arr))