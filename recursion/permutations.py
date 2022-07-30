def swap(a,i,j):
    a=list(a)
    t=a[j]
    a[j]=a[i]
    a[i]=t
    return "".join(a)


def permutations(s,i):
    if i==len(s):
        print(s,end=" ")
    else:
        for j in range(i,len(s)):
            s=swap(s,i,j)
            permutations(s,i+1)
            s=swap(s,j,i)

if __name__ == '__main__':
    permutations("ABCD",i=0)