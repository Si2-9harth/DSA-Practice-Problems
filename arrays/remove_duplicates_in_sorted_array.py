def remove_duplicates(arr):
    if len(arr)==0:
        return
    else:
        res=1
        temp=[]
        temp.append(arr[0])
        for i in range(1,len(arr)):
            if temp[res-1]!=arr[i]:
                temp.append(arr[i])
                res=res+1
    return temp

def remove_duplicates_space(arr):
    if len(arr)==0:
        return
    else:
        res=1
        for i in range(1,len(arr)):
            if arr[res-1]!=arr[i]:
                arr[res]=arr[i]
                res+=1
        return arr[:res]

if __name__ == '__main__':
    print(remove_duplicates_space([1,3,4,2,4,4,5,6,7,7,8]))