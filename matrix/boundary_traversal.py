def b_traversal(mat):
    r=len(mat)
    c=len(mat[0])
    if r==1:
        for i in range(c):
            print(mat[0][i],end=" ")
    elif c==1:
        for i in range(r):
            print(mat[i][0],end=" ")
    else:
        for i in range(c):
            print(mat[0][i],end=" ")
        for i in range(1,r):
            print(mat[i][c-1],end=" ")
        for i in range(c-2,-1,-1):
            print(mat[r-1][i],end=" ")
        for i in range(r-2,0,-1):
            print(mat[i][0],end=" ")


mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
b_traversal(mat)