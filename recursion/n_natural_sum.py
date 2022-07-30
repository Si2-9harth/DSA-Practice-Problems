def n_natural_sum(n):
    if n==1:
        return 1
    else:
        return n+n_natural_sum()

if __name__ =="__main__":
    print(n_natural_sum(5))