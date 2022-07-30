def rotate(arr):
    t=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]=t
    return arr

if __name__ == '__main__':
    print(rotate([1,2,3,4,5,6]))