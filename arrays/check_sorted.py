def sorted(a):
    for i in range(1,len(a)):
        if a[i]<a[i-1]:
            return False
    return True

if __name__ == '__main__':
    print(sorted([1,2,3,5,7,9]))