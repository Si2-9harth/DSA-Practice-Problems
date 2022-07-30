def naive_search(s,p):
    n=len(s)
    m=len(p)
    i=0
    while i<=n-m:
        if p==s[i:i+m]:
            print(i,end=" ")
        i+=1


s="AAAAAAA"
p="AA"
naive_search(s,p)