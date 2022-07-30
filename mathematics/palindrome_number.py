def palindrome(n):
    res=0
    t=n
    while n>0:
        res=res*10+n%10
        n=n//10
    if t==res:
        return True
    else:
        return False

if __name__ =="__main__":
    print(palindrome(343))