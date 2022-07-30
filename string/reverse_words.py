def naive(s):
    l=s.split()
    print(" ".join(l[::-1]))

def reverse(s,start,end):
    while start<=end:
        s[start],s[end]=s[end],s[start]
        start+=1
        end-=1

def efficient(s):
    start=0
    n=len(s)
    t=list(s)
    for end in range(len(s)):
        if t[end]==" ":
            reverse(t,start,end-1)
            start=end+1
    reverse(t,start,n-1)
    reverse(t,0,n-1)
    return "".join(t)

        

s="welcome to gfg"
naive(s)
print(efficient(s))