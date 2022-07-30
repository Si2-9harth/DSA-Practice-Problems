def check_kth(n,k):
    if ((n>>(k-1)) & (1)) ==1:
        return 'Yes'
    else:
        return 'No'

n=13
k=3
print(check_kth(n,k))