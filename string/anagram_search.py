from itertools import count


def check(txt,pat):
    count=[0]*256
    dount=[0]*256
    n=len(txt)
    m=len(pat)
    for i in range(m):
        count[ord(txt[i])]+=1
        dount[ord(pat[i])]+=1
    for i in range(m,n):
        if count==dount:
            return True
        count[ord(txt[i])]+=1
        count[ord(txt[i-m])]-=1

    return False


txt="geeksforgeeks"
pat="fogg"
print(check(txt,pat))