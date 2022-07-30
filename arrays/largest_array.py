def largest(a):
    res=0
    for i in range(1,len(a)):
        if a[res]<a[i]:
            res=i
    return res

#in python arr.index(max(arr))

if __name__ == '__main__':
    print(largest([1,2,45,6,8,98,102,24]))