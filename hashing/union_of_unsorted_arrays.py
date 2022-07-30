def union(a,b):
    a=a+b
    return len(set(a))

a=[10,30,10]
b=[40,10]
print(union(a,b))