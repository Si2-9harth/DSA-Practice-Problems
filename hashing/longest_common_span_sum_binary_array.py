def longest(arr,sum):
    res=0
    d=dict()
    prefix_sum=0
    for i in range(len(arr)):
        prefix_sum+=arr[i]
        if prefix_sum==sum:
            res=i+1
        if prefix_sum not in d.keys():
            d[prefix_sum]=i
        if prefix_sum-sum in d.keys():
            res=max(res,i-d[prefix_sum-sum])
    return res

def longestb(arr1,arr2):
    temp=[]
    for i in range(len(arr1)):
        temp.append(arr1[i]-arr2[i])

    return longest(temp,0)

arr1=[0,1,0,0,0,0]
arr2=[1,0,1,0,0,1]
print(longestb(arr1,arr2))