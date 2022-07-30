# Define a list
z = [3, 7, 4, 2]

# Define a list
z = [3, 7, 4, 2]
# Access the first item of a list at index 0
print(z[0])

# print last item in the list
print(z[-1])

# Define a list
z = [3, 7, 4, 2]
#from index 0 to 1
print(z[0:2])

# everything up to but not including index 3
print(z[:3])

# index 1 to end of list
print(z[1:])

# Defining a list
z = [3, 7, 4, 2]
# Update the item at index 1 with the string "fish"
z[1] = "fish"
print(z)

#print index of value 4 in list
print(z.index(4))

#print index of value 4 but starting start of search from index 3
print(z.index(4, 3))

#count number of times a value occurs in list
random_list = [4, 1, 5, 4, 10, 4]
random_list.count(5)

#sorting
z = [3, 7, 4, 2]
z.sort()
print(z)

# Sorting and Altering original list
# high to low
z.sort(reverse = True)
print(z)

#add to end of list
z = [7, 4, 3, 2]
z.append(3)
print(z)

#remove value from list 
z = [7, 4, 3, 2, 3]
z.remove(2)
print(z)

#pop element from given index
z = [7, 4, 3, 3]
print(z.pop(1))
print(z)

#extend list with another one similar to append
z = [7, 3, 3]
z.extend([4,5])
print(z)
#works the same
print([1,2] + [3,4])

#inserting a index 4
z = [7, 3, 3, 4, 5]
z.insert(4, [1, 2])
print(z)

#reverse a list 
list.reverse()