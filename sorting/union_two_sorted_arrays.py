def union(a,b):
    m=len(a)
    n=len(b)
    i=0
    j=0
    while i<m and j<n:
        if i>0 and a[i]==a[i-1]:
            i=i+1
        elif j>0 and b[j]==b[j-1]:
            j=j+1
        elif a[i]>b[j]:
            print(b[j],end=" ")
            j=j+1
        elif a[i]<b[j]:
            print(a[i],end=" ")
            i=i+1
        else:
            print(a[i],end=" ")
            i=i+1
            j=j+1
    while i<m:
        if i>0 and a[i]==a[i-1]:
            i=i+1
        else:
            print(a[i],end=" ")
            i=i+1
    while j<n:
        if j>0 and b[j]==b[j-1]:
            j=j+1
        else:
            print(b[j],end=" ")
            j=j+1

if __name__ =="__main__":
    a=[2,10,20,20]
    b=[3,20,40]
    union(a,b)