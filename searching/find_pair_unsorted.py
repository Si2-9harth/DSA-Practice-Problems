def pairs(arr,x):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==x:
                return True
    return False


if __name__ =="__main__":
    arr=[3,5,9,2,8,10,11]
    x=17 
    print(pairs(arr,x))