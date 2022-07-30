import bisect

def mat_median(mat):
   r=len(mat)
   c=len(mat[0])
   mini=mat[0][0]
   maxi=0
   for i in range(1,r):
    if mini>mat[i][0]:
        mini=mat[i][0]

    if maxi<mat[i][c-1]:
        maxi=mat[i][c-1]

   med_pos=((r*c) +1)//2
   while mini<maxi:
    mid=mini+(maxi-mini)//2
    mid_pos=[0]
    for i in range(r):
        j=bisect.bisect_right(mat[i],mid)
        mid_pos[0]+=j

    if mid_pos[0]<med_pos:
        mini=mid+1
    else:
        maxi=mid
   return mini

mat=[[5,10,20,30,40],[1,2,3,4,6],[11,13,15,17,19]]
m = [ [1, 3, 5], [2, 6, 9], [3, 6, 9]]
print(mat_median(m))