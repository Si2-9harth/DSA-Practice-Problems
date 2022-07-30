def max_dif(arr):
    res=arr[1]-arr[0]
    min_val=arr[0]
    for i in range(1,len(arr)):
        res=max(arr[i]-min_val,res)
        min_val=min(arr[i],min_val)
    return res

if __name__ == '__main__':
    print(max_dif([2,3,10,6,4,8,1]))