def isdistinct(txt,i,j):
    flag=[False]*256
    for k in range(i,j+1):
        if flag[ord(txt[k])] == True:
            return False
        else:
            flag[ord(txt[k])] = True
    return True


def naive(txt):
    res=1
    for i in range(len(txt)):
        for j in range(i,len(txt)):
            if isdistinct(txt,i,j):
                res=max(res,j-i+1)
    return res

def n_sq(txt):
    visited=[False]*256
    res=1
    for i in range(len(txt)):
        for j in range(i,len(txt)):
            if visited[ord(txt[j])]==True:
                break
            else:
                visited[ord(txt[j])]=True
        res=max(res,j-i+1)
    return res

def efficient(txt):
    n=len(txt)
    res=0
    prev=[-1]*256
    i=0
    for j in range(n):
        i=max(i,prev[ord(txt[j])]+1)
        max_end=j-i+1
        res=max(res,max_end)
        prev[ord(txt[j])]=j
    return res

txt="abac"
print(naive(txt))
print(n_sq(txt))
print(efficient("abcadbd"))