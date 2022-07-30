def reverse(a):
    low=0
    high=len(a)-1
    while high>low:
        temp=a[high]
        a[high]=a[low]
        a[low]=temp
        low=low+1
        high=high-1
    return a

if __name__ == '__main__':
    print(reverse([1,2,45,6,8,98,102,24]))