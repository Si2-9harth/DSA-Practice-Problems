def max_heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        max_heapify(arr,n,largest)

def build_heap(arr,n):
    for i in range(n//2 -1,-1,-1):
        max_heapify(arr,n,i)

def heap_sort(arr,n):
    build_heap(arr,n)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        max_heapify(arr,i,0)

arr=[10,15,50,4,20]
heap_sort(arr,len(arr))
print(arr)