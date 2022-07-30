def check_r(s1,s2,n,m):
    if m==0:
        return True
    elif n==0:
        return False
    elif s1[n-1]==s2[m-1]:
        return check_r(s1,s2,n-1,m-1)
    else:
        return check_r(s1,s2,n-1,m)

def check_i(s1,s2):
    n=len(s1)
    m=len(s2)
    if m>n:
        return False
    else:
        j=0
        i=0
        while i<n and j<m:
            if s1[i]==s2[j]:
                j+=1
            i=i+1
        return j==m

s1="ABCDEF"
s2="ADG"
print(check_i(s1,s2))
n=len(s1)
m=len(s2)
print(check_r(s1,s2,n,m))