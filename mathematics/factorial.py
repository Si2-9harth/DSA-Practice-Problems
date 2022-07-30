def factorial(n):
    if n==0:
        return 1
    else:
        f=1
        for i in range(2,n+1):
            f*=i
        return f

if __name__ == '__main__':
    print(factorial(5))