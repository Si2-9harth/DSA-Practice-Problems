def median_arr(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    if n1>n2:
        median_arr(arr2,arr1)
    else:
        begin=0
        end=n1
        while begin<=end:
            i1=(begin+end)//2
            i2=((n1+n2+1)//2)-i1
            min1=float('inf') if i1==n1 else arr1[i1]
            min2=float('inf') if i2==n2 else arr2[i2]
            max1=float('-inf') if i1==0 else arr1[i1-1]
            max2=float('-inf') if i2==0 else arr2[i2-1]
            if (max1<=min2) and (max2<=min1):
                if (n1+n2)%2==0:
                    return (min(min1,min2)+max(max1,max2))/2
                else:
                    return max(max1,max2)
            else:
                if min2<max1:
                    end=i1-1
                else:
                    begin=i1+1

        

    

if __name__ =="__main__":
    arr1=[30,40,50,60]
    arr2=[5,6,7,8,9]
    print(median_arr(arr1,arr2))    