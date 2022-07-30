def naive(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        return sorted(s1)==sorted(s2)

def efficient(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        count=[0]*256
        for i in range(len(s1)):
            count[ord(s1[i])]+=1
            count[ord(s2[i])]-=1
        if sum(count)==0:
            return True
        else:
            return False

s1="abaac"
s2="aacba"
print(naive(s1,s2))
print(efficient(s1,s2))