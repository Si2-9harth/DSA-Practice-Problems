class interval:
    def __init__(self,start,end):
        self.start=start
        self.end=end

def merge_interval(arr):
    sorted(arr,key=lambda x: x.start)
    res=0
    for i in range(1,len(arr)):
        if arr[res].end>=arr[i].start:
            arr[res].end=max(arr[res].end,arr[i].end)
            arr[res].start=min(arr[res].start,arr[i].start)
        else:
            res=res+1
            arr[res]=arr[i]
    for i in range(res+1):
        print(f"{arr[i].start}, {arr[i].end}",end="  ")


arr=[]
arr.append(interval(5,10))
arr.append(interval(3,15))
arr.append(interval(18,30))
arr.append(interval(2,7))
merge_interval(arr)