def max_sum(arr):
    res=arr[0]
    n=len(arr)
    for i in range(n):
        cur_max=arr[i]
        cur_sum=arr[i]
        for j in range(1,n):
            index=(i+j)%n
            cur_sum+=arr[index]
            cur_max=max(cur_max,cur_sum)
        res=max(cur_max,res)
    return res

def normal_max_sum(arr):
    res=arr[0]
    n=len(arr)
    max_ending=arr[0]
    for i in range(1,n):
        max_ending=max(max_ending+arr[i],arr[i])
        res=max(res,max_ending)
    return res


def max_summ(arr):
    n=len(arr)
    max_normal=normal_max_sum(arr)
    if max_normal<0:
        return max_normal
    else:
        arr_sum=0
        for i in range(n):
            arr_sum+=arr[i]
            arr[i]=-1*arr[i]
        max_circular=arr_sum+normal_max_sum(arr)
    return max(max_circular,max_normal)

if __name__ == '__main__':
    print(max_summ([8,-4,3,-5,4]))