def symbol(a,b):
    return (a=="{" and b=="}") or (a=="(" and b==")") or (a=="[" and b=="]")

def check(s):
    st=[]
    for i in s:
        if i=="{" or i=="[" or i=="(":
            st.append(i)
        else:
            if len(st)==0:
                return "No"
            else:
                if symbol(st[-1],i):
                    st.pop()
                else:
                    return "No"
    if len(st)==0:    
        return "Yes"
    else:
        return "No"

print(check("({[()]})"))
print(check("({[)(]})"))
print(check("{}([()])"))