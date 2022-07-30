def check(arr,sum):
    s=set()
    for i in arr:
        if sum-i in s:
            return True
        else:
            s.add(i)
    return False

arr=[8,3,4,2,5]
print(check(arr,20))