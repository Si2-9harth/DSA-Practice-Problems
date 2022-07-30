def print_flips(arr):
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            if arr[i]!=arr[0]:
                print("From",i,"to",end=" ")
            else:
                print(i-1)
    if arr[len(arr)-1]!=arr[0]:
        print(len(arr)-1)


if __name__ =="__main__":
    arr=[0,0,1,1,0,0,1,1,0,1]
    print_flips(arr)