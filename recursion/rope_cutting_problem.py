def max_cuts(n,a,b,c):
    if n<0:
        return -1
    if n==0:
        return 0
    res=max(max_cuts(n-a,a,b,c),max_cuts(n-b,a,b,c),max_cuts(n-c,a,b,c))
    if res==-1:
        return -1
    return res+1

if __name__ == "__main__":
    print(max_cuts(23,11,9,12))