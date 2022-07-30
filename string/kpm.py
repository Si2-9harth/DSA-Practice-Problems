def prefix(txt):
    a=[]
    k=""
    a.append(k)
    for i in range(len(txt)-1):
        k=k+txt[i]
        a.append(k)
    return a
def suffix(txt):
    a=[]
    k=""
    a.append(k)
    n=len(txt)
    i=-1
    while -1*i<=n:
        a.append(txt[i:])
        i-=1
    return a

def longest(p,s):
    res=0
    for i in p:
        if i in s:
            res=max(res,len(i))
    return res

def lps(txt):
    n=len(txt)
    a=[]
    for i in range(1,n+1):
        p=prefix(txt[:i])
        s=suffix(txt[:i])
        val=longest(p,s)
        a.append(val)
    return a

def lps_e(txt):
    i=1
    n=len(txt)
    l=0
    lps=[]
    lps.append(0)
    while i<n:
        if txt[l]==txt[i]:
            l+=1
            lps.append(l)
            i+=1
        else:
            if l==0:
                lps.append(l)
                i+=1
            else:
                l=lps[l-1]
    return lps


txt="ababacab"
print(lps(txt))
print(lps_e(txt))