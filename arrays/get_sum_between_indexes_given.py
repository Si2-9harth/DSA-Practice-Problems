def prefix_sum(arr):
    s_arr=[]
    s_arr.append(arr[0])
    for i in range(1,len(arr)):
        s_arr.append(arr[i]+s_arr[i-1])
    return s_arr

def get_sum(arr,l,r):
    s_arr=prefix_sum(arr)
    if l==0:
        return s_arr[r]
    else:
        return s_arr[r]-s_arr[l-1]

if __name__ =="__main__":
    arr=[2,8,3,9,6,5,4]
    print(get_sum(arr,1,3))