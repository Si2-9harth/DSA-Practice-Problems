def check(arr,sum):
    prefix_sum=0
    s=set()
    for i in arr:
        prefix_sum+=i
        if prefix_sum==sum:
            return True
        if prefix_sum-sum in s:
            return True
        s.add(prefix_sum)
    return False

arr=[5,8,6,13,3,-1]
sum=13
print(check(arr,sum))