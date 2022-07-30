def frequencies(arr):
    f=1
    n=len(arr)
    i=1
    while i<n:
        while (i<n) and (arr[i]==arr[i-1]):
            f=f+1
            i=i+1
        print("{} {}".format(arr[i-1],f))
        i=i+1
        f=1
    if n==1 or arr[n-1]!=arr[n-2]:
        print("{} {}".format(arr[n-1],1))

if __name__ == '__main__':
    frequencies([10,10,10,30,30,40])
    print("----------------------------------------------------------------------------------------------------------")
    frequencies([40,50,50,50])