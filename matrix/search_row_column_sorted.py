def search(mat,x):
    r=len(mat)
    c=len(mat[0])
    i=0
    j=c-1
    while i<r and j>=0:
        if mat[i][j]==x:
            print(f"found {x} at {i},{j}")
            return
        elif mat[i][j]>x:
            j-=1
        else:
            i+=1
    print("not found")        

mat=[[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
x=12
search(mat,x)