def palindrome(s,start,end):
    if start>=end:
        return True
    else:
        return (s[start]==s[end]) and (s[start+1]==s[end-1])

if __name__ == '__main__':
    st=input("Please enter string you want to check: ")
    print(palindrome(st,0,len(st)-1))