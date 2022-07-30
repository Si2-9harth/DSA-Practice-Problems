class Stack():
    def __init__(self):
        self.arr=[]
    
    def push(self,val):
        self.arr.append(val)

    def is_empty(self):
        return self.arr==[]
    
    def pop(self):
        if self.is_empty():
            print("Empty stack")
        else:
            res=self.arr[-1]
            self.arr.pop()
            return res
    def peek(self):
        if self.is_empty():
            print("Empty stack")
            return "Error"
        else:
            return self.arr[-1]
    def size(self):
        return len(self.arr)

s=Stack()
s.push(5)
s.push(10)
s.push(20)
print(s.pop())
print(s.size())
print(s.peek())
print(s.is_empty())


    