def trailing(n):
    i=5
    f=0
    while i<=n:
        f=f+(n//5)
        i*=5
    return f
if __name__ =="__main__":
    print(trailing(15))