def frequencies(s):
    count=[0]*26
    for i in s:
        count[ord(i)-ord('a')]+=1
    for i in range(len(count)):
        if count[i]>0:
            print("{} == {}".format(chr(i+ord('a')),count[i]))

s="geeksforgeeks"
frequencies(s)