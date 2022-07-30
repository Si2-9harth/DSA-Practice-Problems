def intersection(a,b):
    a=set(a)
    b=(b)
    return [i for i in a if i in b]

def naive(a,b):
    m=len(a)
    n=len(b)
    for i in range(m):
        if i>0 and a[i]==a[i-1]:
            pass
        else:
            for j in range(n):
                if a[i]==b[j]:
                    print(a[i])
                    break

def efficient(a,b):
    m=len(a)
    n=len(b)
    i=0
    j=0
    while(i<m and j<n):
        if i>0 and a[i]==a[i-1]:
            i=i+1
            pass
        elif a[i]>b[j]:
            j=j+1
        elif a[i]<b[j]:
            i+=1
        else:
            print(a[i],end=' ')
            i=i+1
            j=j+1



a=[3,5,10,10,10,15,15,20]
b=[5,10,10,15,30]
efficient(a,b)