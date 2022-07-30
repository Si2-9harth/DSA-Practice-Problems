def isprime(n):
    if n==1:
        return False
    elif n==2 or n==3:
        return True
    elif n%2==0 or n%3==0:
        return False
    else:
        i=5
        while i*i<=n:
            if n%i==0 or n%(i+2)==0:
                return False
            i=i+6
        return True


def sieve(n):
    primes=[True]*(n+1)
    i=2
    while i*i<=n:
        if isprime(i):
            j=2*i
            while j<=n:
                primes[j]=False
                j=j+i
        i+=1
    for i in range(2,n+1):
        if primes[i]==True:
            print(i,end=" ")
    return

def sieve_new(n):
    primes=[True]*(n+1)
    i=2
    while i*i<=n:
        if primes[i]:
            j=2*i
            while j<=n:
                primes[j]=False
                j=j+i
        i+=1
    for i in range(2,n+1):
        if primes[i]==True:
            print(i,end=" ")
    return

if __name__ == "__main__":
    sieve_new(20)
