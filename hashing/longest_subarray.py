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

arr=[8,-4,4,-4,4,-4,2,2]
sum=4
print(longest(arr,sum))