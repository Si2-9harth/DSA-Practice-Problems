def prime(n):
    if n==1:
        return False
    elif n==2 or n==3:
        return True
    elif n%2==0 or n%3==0:
        return False
    else:
        i=5
        while i<n:
            if n%i==0 or n%(i+2)==0:
                return False
            i+=6
        return True


if __name__ == '__main__':
    print(prime(29))