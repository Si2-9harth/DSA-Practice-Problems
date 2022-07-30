def count_naive(n):
    res=0
    while n>0:
        if n&1==1:
            res=res+1
        n=n>>1
    return res
def brian_kerningam(n):
    res=0
    while n>0:
        n=n&(n-1)
        res+=1
    return res

n=13
print(count_naive(n))
print(brian_kerningam(n))