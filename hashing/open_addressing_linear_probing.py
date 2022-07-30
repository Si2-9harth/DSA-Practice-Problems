class Myhash():
    def __init__(self,capacity):
        self.capacity = capacity
        self.size=0
        self.arr=[-1]*self.capacity
    
    def hashing(self,key):
        return key%self.capacity
    
    def search(self,key):
        h=self.hashing(key)
        i=h
        while i!=-1:
            if self.arr[i]==key:
                return True
            i=(i+1)%self.capacity
            if i==h:
                return False
        return False
    
    def insert(self,key):
        if self.size==self.capacity:
            return False
        else:
            i=self.hashing(key)
            while self.arr[i]!=-1 and self.arr[i]!=key and self.arr[i]!=-2:
                i=(i+1)%self.capacity

            if self.arr[i]==key:
                return False
            else:
                self.arr[i]=key
                self.size+=1
                return True

    def erase(self,key):
        h=self.hashing(key)
        i=h
        while self.arr[i]!=-1:
            if self.arr[i]==key:
                self.arr[i]=-2
                self.size-=1
                return True
            i=(i+1)%self.capacity
            if i==h:
                return False
        return False


    def print_hash(self):
        print("The hash is->")
        print(self.arr)



ht=Myhash(7)
ht.print_hash()
ht.insert(49)
ht.insert(56)
ht.insert(72)
ht.print_hash()
print(ht.search(56))
ht.erase(56)
ht.print_hash()
print(ht.search(56))

