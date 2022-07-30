def snake_pattern(mat):
    r=len(mat)
    c=len(mat[0])
    for i in range(r):
        if i%2==0:
            for j in range(c):
                print(mat[i][j],end=" ")
        else:
            for j in range(c-1,-1,-1):
                print(mat[i][j],end=" ")

mat=[]
for i in range(4):
    a=[]
    for j in range(4):
        a.append(int(input()))
    mat.append(a)
snake_pattern(mat)