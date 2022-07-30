def majority(arr):
    n=len(arr)
    for i in range(n):
        count=0
        for j in range(n):
            if arr[j]==arr[i]:
                count=count+1
        if count>n//2:
            return i
    return -1

def majorityy(arr):
    n=len(arr)
    max_count=arr.count(arr[0])
    for i in range(n):
        cur=arr.count(arr[i])
        max_count=max(cur,max_count)
    
    for i in range(n):
        if (arr.count(arr[i])==max_count) and (max_count>n//2):
            return i
    return -1

def majorityyy(arr):
    n=len(arr)
    temp=set(arr)
    temp=list(temp)
    t=[]
    for i in temp:
        t.append(arr.count(i))
    maximum_counts=max(t)
    if maximum_counts>n//2:
        index=t.index(maximum_counts)
        val=temp[index]
        return arr.index(val)
    else:
        return -1    

def efficient_majority(arr):
    res=0
    n=len(arr)
    count=1
    for i in range(1,n):
        if arr[res]==arr[i]:
            count+=1
        else:
            count-=1
        if count==0:
            count=1
            res=i
    
    count=0
    for i in range(n):
        if arr[res]==arr[i]:
            count+=1
    if count>n//2:
        return i
    return -1

if __name__ =="__main__":
    arr=[8,7,6,8,6,6,6,6]
    print(efficient_majority(arr))
