def odd_occuring(arr):
    res=0
    for i in arr:
        res=res^i
    return res

def find_missing(arr):
    a=0
    n=len(arr)
    for i in range(1,n+2):
        a=a^i
    b=0
    for i in arr:
        b=b^i
    return a^b

arr=[4,3,4,4,5,5,4]
print(odd_occuring(arr))

#given an array of n number that has range of values from 1 to n+1. 
# Every number appear only once. Hence one number is missing. Find missing number.
arrr=[1,2,5,3]
print(find_missing(arrr))
