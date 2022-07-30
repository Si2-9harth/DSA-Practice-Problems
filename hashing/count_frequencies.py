def freq(arr):
    s=set(arr)
    d=dict.fromkeys(s,0)
    for i in arr:
        d[i]+=1
    print(sorted(d.items()))

arr=[20,30,10,20,10,20,30]
freq(arr)