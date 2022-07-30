def rotated(mat):
    r=len(mat)
    c=len(mat[0])
    for i in range(r):
        for j in range(i+1,c):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    
    for i in range(c):
        low=0
        high=c-1
        while low<high:
            mat[low][i],mat[high][i]=mat[high][i],mat[low][i]
            low=low+1
            high=high-1

mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print("given matrix is:")
for i in range(4):
    for j in range(4):
        print(mat[i][j],end=" ")
    print()

rotated(mat)

print("rotated matrix is:")
for i in range(4):
    for j in range(4):
        print(mat[i][j],end=" ")
    print()