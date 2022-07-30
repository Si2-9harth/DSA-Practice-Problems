def move_zero(a):
    count=0
    for i in range(len(a)):
        if a[i]!=0:
            t=a[i]
            a[i]=a[count]
            a[count]=t
            count+=1

    return a

if __name__ == '__main__':
    print(move_zero([1,0,45,60,70,0,0,3,0,3]))