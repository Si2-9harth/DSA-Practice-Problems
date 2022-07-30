d=256
def rabin_karp(txt,pat):
    n=len(txt)
    m=len(pat)
    h=1
    q=101
    i=0
    j=0
    p=0
    t=0
    for i in range(m-1):
        h=(h*d)%q

    for i in range(m):
        p=(p*d+ord(pat[i]))%q
        t=(t*d+ord(txt[i]))%q
    
    for i in range(n-m+1):
        if p==t:
            for j in range(m):
                if txt[i+j]!=pat[j]:
                    break
            if j==m-1:
                print(i,end=" ")
        if i<n-m:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+m]))%q
            if t<0:
                t=t+q
            
    



txt="abdabcbabc"
pat="abc"
rabin_karp(txt,pat)