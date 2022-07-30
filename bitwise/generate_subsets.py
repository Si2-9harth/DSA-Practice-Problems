def generate_subsets(s):
    n=len(s)
    pow_size=2**n
    for counter in range(pow_size):
        for j in range(n):
            if ((counter&(j<<1))!=0):
                print(s[j],end="")
        print("")


s="abc"
generate_subsets(s)