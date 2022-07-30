def naive(s):
    for i in range(len(s)):
        flag=False
        for j in range(len(s)):
            if i!=j and s[i]==s[j]:
                flag=True
                break
        if flag==False:
            return i
    return -1

def better(s):
    count=[0]*256
    for i in s:
        count[ord(i)]+=1
    for i in range(len(s)):
        if count[ord(s[i])]==1:
            return i
    return -1

def efficient(s):
    count=[-1]*256
    for i in range(len(s)):
        if count[ord(s[i])]==-1:
            count[ord(s[i])]=i
        else:
            count[ord(s[i])]=-2
    for i in count:
        if i>0:
            return i
    return -1

s="geeksforgeeks"
print(naive(s))
print(better(s))
print(efficient(s))