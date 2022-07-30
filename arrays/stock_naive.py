def max_profit(arr,start,end):
    if end<=start:
        return 0
    else:
        profit=0
        for i in range(start,end):
            for j in range(i+1,end+1):
                if arr[j]>arr[i]:
                    cur_profit=arr[j]-arr[i]+max_profit(arr,start,i-1)+max_profit(arr,j+1,end)
                    profit=max(profit,cur_profit)
    return profit

if __name__ == '__main__':
    arr=[1,5,3,8,12]
    print(max_profit(arr,0,len(arr)-1))