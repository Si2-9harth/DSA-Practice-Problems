def check(n):
    if n==0:
        return False
    else:
        return (n&(n-1)==0)

n1=32
n2=6
print(check(n1))
print(check(n2))
