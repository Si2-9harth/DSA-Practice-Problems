def max_profit(arr):
    profit=0
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            profit=profit+arr[i]-arr[i-1]
    return profit

if __name__ == '__main__':
    arr=[1,5,3,8,12]
    print(max_profit(arr))