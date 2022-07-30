def merge(a,b):
    c=[]
    n1=len(a)
    n2=len(b)
    i=0
    j=0
    while i<n1 and j<n2:
        if a[i]>b[j]:
            c.append(b[j])
            j=j+1
        else:
            c.append(a[i])
            i=i+1
    
    if j<n2:
        c=c+b[j:]
    else:
        c=c+a[i:]
    return c

if __name__ =="__main__":
    a=[10,20,35]
    b=[5,50,50]
    print(merge(a,b))