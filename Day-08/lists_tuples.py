#lists
my_list = [1, 2, 3, 4, "apple", "cat", "dog", 7.5, 3.14]
my_list2 = [1, 45, 34, 67, 22, 23, 90, 11, 24]

#print my_list
print("Intial List : ", my_list)
print ("Intial Numbered List : ", my_list2)

#append new element to list
my_list.append("ball")


#remove element from list
my_list.remove(3.14)

#get index value of an element
index = my_list.index("apple")
print("Index of apple is: ", index)

# to get a dog from the my_list
print("Get certain element: ", my_list[6])

#slice my_list2 elements from 34 to 90
sliced_list = my_list2[2:7]
print("Sliced list: ", sliced_list)


#sort a list 
my_list2.sort()
sorted_list = my_list2
print("Sorted List: ", sorted_list)

new_list = my_list

#print new_list
print("New List : ", new_list)

#print length 
print("Length of the list: ", len(new_list))

#----------------------------------------------------------------------

#tuple
my_tuple = ("amazon", "microsoft", "meta", "apple", "tesla")
print("My initial tuple : ", my_tuple)

#concatenate mutiple tuples
new_tuple = my_tuple + ("blackberry", 3.14) + ("intuit", "square")
print("Concatenated tuple : ", new_tuple)

# Using Tuples for Multiple Return Values
# Tuples are often used to return multiple values from a function.

def get_coordinates():
    return (3, 4)

x, y = get_coordinates()

print("Value of x:", x, "&", "Value of y:",y)


