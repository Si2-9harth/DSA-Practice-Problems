import random

def hoare(arr,l,h):
    i=l-1
    j=h+1
    p=random.randint(l,h)
    arr[p],arr[l]=arr[l],arr[p]
    pivot=arr[l]
    while True:
        i=i+1
        while arr[i]<pivot:
            i=i+1
        j=j-1
        while arr[j]>pivot:
            j=j-1
        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i]

def tail_quick(arr,l,h):
    while l<h:
        p=hoare(arr,l,h)
        if p-l<h-p:
            tail_quick(arr,l,p)
            l=p+1
        else:
            tail_quick(arr,p+1,h)
            h=p-1

def quick_hoare(arr,l,h):
    if l<h:
        p=hoare(arr,l,h)
        quick_hoare(arr,l,p)
        quick_hoare(arr,p+1,h)

  


arr=[10,80,30,90,40,50,70]
l=0
h=len(arr)-1
tail_quick(arr,l,h)
print(arr)