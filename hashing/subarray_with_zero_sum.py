def check(arr):
    s=set()
    prefix_sum=0
    for i in arr:
        prefix_sum+=i
        if prefix_sum in s:
            return True
        if prefix_sum==0:
            return True
        s.add(prefix_sum)
    return False

arr=[3,4,3,1,1]
print(check(arr))