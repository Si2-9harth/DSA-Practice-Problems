def check_odds(arr):
    xor=0
    res1=0
    res2=0
    for i in arr:
        xor=xor^i
    sn=xor&(~(xor-1))
    for i in arr:
        if (i&sn)!=0:
            res1=res1^i
        else:
            res2=res2^i
    print(res1,res2)

arr=[3,4,3,4,5,4,4,6,7,7]
check_odds(arr)