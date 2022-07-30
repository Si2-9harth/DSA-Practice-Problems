def display_hash(hash_table):
    f=0
    for i in hash_table:
        print(f,end="")
        f=f+1
        for j in i:
            print("-->",end=" ")
            print(j,end=" ")
        print()

def hash(key):
    return key%7

def insert(hash_table,val):
    key=hash(val)
    hash_table[key].append(val)

def delete(hash_table,val):
    key=hash(val)
    hash_table[key].remove(val)

def search(hash_table,val):
    key=hash(val)
    return val in hash_table[key]

keys=[70,71,9,56,72,59]
hash_table=[[] for _ in range(7)]

for i in keys:
    insert(hash_table,i)

display_hash(hash_table)

delete(hash_table,70)
print(search(hash_table,70))
print(search(hash_table,9))
display_hash(hash_table)
