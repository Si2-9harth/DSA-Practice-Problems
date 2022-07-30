def palindrome(s):
    return s==s[::-1]

def palindromee(s):
    begin=0
    end=len(s)-1
    while begin<end:
        if s[begin]!=s[end]:
            return False
        begin+=1
        end-=1
    return True

s="abba"
print(palindrome(s))
print(palindromee(s))