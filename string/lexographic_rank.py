from itertools import count


def factorial(n):
    if n==0:
        return 1
    else:
        f=1
        for i in range(2,n+1):
            f*=i
        return f

def rank(txt):
    n=len(txt)
    a=list(txt)
    a=sorted(a)
    res=1
    for i in range(len(txt)):
        n=n-1
        ind=a.index(txt[i])
        res+=ind*factorial(n)
        a.remove(txt[i])
    return res

def rankk(txt):
    n=len(txt)
    res=1
    mul=factorial(len(txt))
    counts=[0]*256
    for i in range(len(txt)):
        counts[ord(txt[i])]+=1
    for i in range(1,256):
        counts[i]=counts[i-1]+counts[i]
    for i in range(n):
        mul/=n-i
        res+=counts[ord(txt[i])-1]*mul
        for j in range(ord(txt[i]),256):
            counts[j]-=1  
    return int(res)      
    


txt="string"
print(rank(txt))
print(rank("abcd"))
print("----------------------------------efficient--------------------------------")
print(rankk(txt))
print(rankk("abcd"))