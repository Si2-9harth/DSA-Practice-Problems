import random

def partition(arr,l,h):
    p=random.randint(l,h)
    arr[p],arr[h]=arr[h],arr[p]
    pivot=arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    i=i+1
    arr[i],arr[h]=arr[h],arr[i]
    return i

def quick_lomuto(arr,l,h):
    if l<h:
        p=partition(arr,l,h)
        quick_lomuto(arr,l,p-1)
        quick_lomuto(arr,p+1,h)

def tail_quick(arr,l,h):
    
    while l<h:
        p=partition(arr,l,h)
        if p-l<h-p:
            tail_quick(arr,l,p-1)
            l=p+1
        else:
            tail_quick(arr,p+1,h)
            h=p-1  

arr=[10,80,30,90,40,50,70]
l=0
h=len(arr)-1
quick_lomuto(arr,l,h)
print(arr)