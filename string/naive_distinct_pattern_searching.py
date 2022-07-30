def naive_pattern(s,p):
    n=len(s)
    m=len(p)
    i=0
    while i<=n-m:
        for j in range(m):
            if s[i+j]!=p[j]:
                break
            j=j+1
        if j==m:
            print(i,end=" ")
        if j==0:
            i=i+1
        else:
            i=i+j-1



s="ABCABCD"
p="ABCD"
naive_pattern(s,p)