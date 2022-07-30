class stack:
    def __init__(self):
        self.s=[]
        self.a=[]
    
    def push(self,val):
        self.s.append(val)
        if len(self.a)==0 or self.s[-1]<=self.a[-1]:
            self.a.append(val)
    def pop(self):
        if self.s[-1]==self.a[-1]:
            self.s.pop()
            self.a.pop()
        else:
            self.s.pop()
    def mini(self):
        return self.a[-1]

class stackk:
    def __init__(self):
        self.s=[]
        self.min=None

    def isempty(self):
        return self.s==[]

    def push(self,val):
        if self.isempty():
            self.min=val
            self.s.append(val)
        elif self.min>=val:
            self.s.append(val-self.min)
            self.min=val
        else:
            self.s.append(val)

    def pop(self):
        t=self.s.pop()
        if t<=0:
            res=self.min
            self.min=self.min-t
            return res
        else:
            return t

    def mini(self):
        return self.min

class stackkk:
    def __init__(self):
        self.min=None
        self.s=[]
    def top(self):
        t=self.s[-1]
        if t<=self.min:
            return self.min
        else:
            return t
        
    def isempty(self):
        return self.s==[]

    def push(self,val):
        x=val
        if self.isempty():
            self.min=x
            self.s.append(x)
        elif self.min>=x:
            self.s.append((2*x)-self.min)
            self.min=x
        else:
            self.s.append(x)

    def pop(self):
        t=self.s.pop()
        if t<=self.min:
            res=self.min
            self.min=(2*self.min)-t
            return res
        else:
            return t
    def mini(self):
        return self.min






s=stackkk()
s.push(20)
s.push(10)
print(s.mini())
s.push(5)
#print(s.a)
print(s.mini())
print(s.pop())
print(s.mini())
print(s.pop())
print(s.mini())

