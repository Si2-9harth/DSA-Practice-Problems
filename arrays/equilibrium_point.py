def eq_point(arr):
    sum_arr=0
    n=len(arr)
    for i in arr:
        sum_arr+=i
    left=0
    for i in range(n):
        if left==sum_arr-arr[i]:
            return True
        else:
            left=left+arr[i]
            sum_arr=sum_arr-arr[i]
    return False

if __name__ =="__main__":
    arr=[3,4,8,-9,20,6]
    print(eq_point(arr))