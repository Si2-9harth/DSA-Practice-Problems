def second_largest(a):
    largest=max(a)
    res=-1
    for i in range(len(a)):
        if a[i]!=largest:
            if res==-1:
                res=i
            elif a[res]<a[i]:
                res=i
    return res

def better_second_largest(a):
    largest=0
    res=-1
    for i in range(len(a)):
        if a[i]>a[largest]:
            res=largest
            largest=i 
        elif res==-1 or a[res]<a[i]:
            res=i
    return res

if __name__ == '__main__':
    print(better_second_largest([1,2,45,6,8,98,102,24]))