def pairs(arr,x,low,high):
    while low<high:
        if arr[low]**2 +arr[high]**2==x:
            return True
        elif arr[low]**2 +arr[high]**2>x:
             high=high-1
        else:
            low=low+1
    return False

def triplets_hyp(arr):
    for i in range(len(arr)):
        if pairs(arr,i**2,0,len(arr)-1):
            return True



if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7,8,9,10]
    print(triplets_hyp(arr))
