def prefix_sum(arr):
    s=[]
    s.append(arr[0])
    for i in range(1,len(arr)):
        s.append(s[i-1]+arr[i])
    return s

def elements(l,r):
    n=len(l)
    arr=[0]*1000
    for i in range(n):
        arr[l[i]]=arr[l[i]]+1
        arr[r[i]+1]=arr[r[i]+1]-1
    prefix_arr=prefix_sum(arr)
    maxs=prefix_arr[0]
    res=0
    for i in range(len(prefix_arr)):
        if prefix_arr[i]>maxs:
            res=i
            maxs=prefix_arr[i]
    return res

if __name__ == "__main__":
    l=[1,2,3]
    r=[3,5,7]
    print(elements(l,r))


#Q1 check if given array can be divided into 3 parts with equal sum
#Q2 check if there is subarray with zero as sum
#Q3 find longest subarray with equal number of zeros and ones in binary array.