def intersection(a,b):
    x=set(a)
    y=set(b)
    z=x.intersection(y)
    return len(z)

def intersection_x(a,b):
    x=set(a)
    res=0
    for i in b:
        if i in x:
            res+=1
            x.discard(i)
    return res
a=[10,20,10,30,20]
b=[20,10,10,40]
print(intersection(a,b))
print(intersection_x(a,b))