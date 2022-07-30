import math
def digits_factorial(n):
    s=1
    for i in range(2,n+1):
        s=s+math.log(i,10)
    return math.floor(s)

if __name__ == '__main__':
    print(digits_factorial(5))