def transpose(mat):
    r=len(mat)
    c=len(mat[0])
    for i in range(r):
        for j in range(i+1,c):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]

mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print("given matrix is:")
for i in range(4):
    for j in range(4):
        print(mat[i][j],end=" ")
    print()

transpose(mat)

print("transposed matrix is:")
for i in range(4):
    for j in range(4):
        print(mat[i][j],end=" ")
    print()