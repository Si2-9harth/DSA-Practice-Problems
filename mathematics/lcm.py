def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return int((a*b)/gcd(a,b))
if __name__ =="__main__":
    print(lcm(6,4))