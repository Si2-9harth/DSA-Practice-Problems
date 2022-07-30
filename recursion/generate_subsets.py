def subsequences(s,cur,index):
    if index==len(s):
        print(cur,end=' ')
    else:
        subsequences(s,cur,index+1)
        subsequences(s,cur+s[index],index+1)

if __name__ == "__main__":
    subsequences("ABC","",0)
