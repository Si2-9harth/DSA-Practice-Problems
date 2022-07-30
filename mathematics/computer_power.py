def computing_power(n,p):
    if p==0:
        return 1
    else:
        t=computing_power(n,p//2)
        if p%2==0:
            return t*t
        else:
            return t*t*n

if __name__ == '__main__':
    print(computing_power(3,5))