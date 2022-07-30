def josephusProblem(n,k):
    if n==1:
        return 0
    else:
        return (josephusProblem(n-1,k)+k)%n
def index_1(n,k):
    return josephusProblem(n,k)+1
    
if __name__ == '__main__':
    print(josephusProblem(4,3))