def count_digits(n):
    if n==0:
        return 0
    else:
        return 1+count_digits(n//10)

if __name__ == '__main__':
    print(count_digits(345))