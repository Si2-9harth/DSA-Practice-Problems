def subset_sum(arr,sum,i):
    if i==len(arr):
        if sum==0:
            return 1
        else:
            return 0
    return subset_sum(arr,sum,i+1) + subset_sum(arr,sum-arr[i],i+1)

if __name__ == '__main__':
    print(subset_sum([10,20,15],25,0))