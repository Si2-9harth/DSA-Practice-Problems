def check(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        return s2 in s1+s1


s1="ABCD"
s2="CDAA"
print(check(s1,s2))