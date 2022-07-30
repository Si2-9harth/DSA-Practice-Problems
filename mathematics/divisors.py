def divisors(n):
    i=1
    while i*i<n:
        if n%i==0:
            print(i)
        i+=1
    while i>0:
        if n%i==0:
            print(int(n/i))
        i-=1
    return

if __name__ == '__main__':
    divisors(14)