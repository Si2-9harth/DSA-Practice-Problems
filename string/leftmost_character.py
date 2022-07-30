def lmost(s):
    n=len(s)
    for i in range(n):
        for j in range(i+1,n):
            if s[i]==s[j]:
                return i
    return -1

def leftmost(s):
    count=[0]*256
    for i in s:
        count[ord(i)]+=1
    for i in range(len(s)):
        if count[ord(s[i])]>1:
            return i
    return -1

def lfmost(s):
    count=[-1]*256
    res=float('inf')
    for i in range(len(s)):
        if count[ord(s[i])]==-1:
            count[ord(s[i])]=i
        else:
            res=min(res,count[ord(s[i])])
    if res==float('inf'):
        return -1
    else:
        return res

def ltmost(s):
    count=[False]*256
    res=-1
    for i in range(len(s)-1,-1,-1):
        if count[ord(s[i])]:
            res=i
        else:
            count[ord(s[i])]=True
    return res


s="abccbd"
print(lmost(s))
print(leftmost(s))
print(lfmost(s))
print(ltmost(s))  