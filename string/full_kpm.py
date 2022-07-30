def lps(txt):
    lp=[]
    l=0
    lp.append(0)
    i=1
    while i<len(txt):
        if txt[i]==txt[l]:
            l+=1
            lp.append(l)
            i+=1
        else:
            if l==0:
                lp.append(l)
                i+=1
            else:
                l=lp[l-1]

    return lp

def kpm(txt,pat):
    lp=lps(pat)
    n=len(txt)
    m=len(pat)
    i=0
    j=0
    while i<n:
        if txt[i]==pat[j]:
            i+=1
            j+=1
        if j==m:
            print(i-j)
            j=lp[j-1]
        elif i<n and pat[j]!=txt[i]:
            if j==0:
                i+=1
            else:
                j=lp[j-1]

txt="ababcababaad"
pat="ababa"
kpm(txt,pat)